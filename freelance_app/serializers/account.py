import re
from django.contrib.auth.hashers import check_password
from freelance_app.common_utils.custom_handler import CustomValidationError
from freelance_app.common_utils.token import get_token
from freelance_app.common_utils.validate_password import validate_password
from freelance_app.models import User
from rest_framework import serializers
from freelance_app.models.user import UserPvc
from django.utils.functional import cached_property


class AuthSerializer(serializers.Serializer):
    """ Сериалайзер для авторизации пользователя """
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    redirect_url = serializers.CharField(read_only=True)

    @cached_property
    def fields(self):
        fields = super(AuthSerializer, self).fields
        from_login = self._get_login_params(self.context['request'])
        if from_login == 'email':
            fields['email'] = serializers.CharField(write_only=True)
        else:
            fields['username'] = serializers.CharField(write_only=True)

        return fields

    @staticmethod
    def _get_login_params(request):
        login_params = request.query_params.get('login_params')
        if login_params is None:
            raise CustomValidationError({'login_params': 'Ошибка в выборе типа авторизации (почта, логин)'})
        return login_params

    def _get_user(self, validated_data):
        from_login = self._get_login_params(self.context['request'])
        if from_login == 'email':
            return User.objects.get(email=validated_data['email'])
        elif from_login == 'username':
            return User.objects.get(username=validated_data['username'])
        raise CustomValidationError('login_params', 'Не заданы параметры запроса: Выберите один - email, '
                                                    'username')

    def validate(self, attrs):
        try:
            user = self._get_user(attrs)
            if not check_password(attrs.get('password'), user.password):
                raise CustomValidationError({'message': 'Логин или пароль неверный'})
        except User.DoesNotExist:
            raise CustomValidationError({'message': 'Логин или пароль неверный'})
        return attrs

    def create(self, validated_data):
        try:
            user = self._get_user(validated_data)
            token = get_token(self.context['request'], user)
            return {
                'access': str(token.access_token),
                'refresh': str(token)
            }
        except User.DoesNotExist:
            return {
                'redirect_url': f"{self.context['request'].scheme}://{self.context['request'].get_host()}"
                                f"/api/freelance_app/account/create/"
            }


class AccountCreateSerializer(serializers.ModelSerializer):
    """ Сериалайзер для регистрации пользователя """
    email = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    verified_password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    patronymic = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    pvc = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
            'verified_password',
            'first_name',
            'surname',
            'patronymic',
            'phone',
            'pvc'
        )
        write_only_fields = ('password', 'verified_password', 'pvc')

    @staticmethod
    def validate_email(value):
        if User.objects.filter(email=value).exists():
            raise CustomValidationError({'email': 'Почта занята другим пользователем'})
        return value

    @staticmethod
    def validate_password(value):
        if not validate_password(value)[0] is True:
            raise CustomValidationError({'password': validate_password(value)[1]})

        return value

    @staticmethod
    def validate_phone(value):
        if User.objects.filter(phone=value).exists():
            raise CustomValidationError({'phone': 'Номер телефона занят другим пользователем'})

        phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
        if not phone_pattern.match(value):
            raise CustomValidationError({'phone': 'Введён некорректный номер телефона'})

        return value

    def validate(self, data):
        if not UserPvc.objects.filter(email=data['email'], pvc=data['pvc']).exists():
            raise CustomValidationError({'pvc':  'Неверный код'})
        return data

    def create(self, validated_data):
        UserPvc.objects.filter(email=validated_data.get('email'), pvc=validated_data.get('pvc')).delete()

        if validated_data['verified_password'] != validated_data['password']:
            raise CustomValidationError({'verified_password': 'Пароли не совпадают'})

        validated_data.pop('verified_password')
        validated_data.pop('pvc')
        instance: User = super(AccountCreateSerializer, self).create(validated_data)
        # хэш пароля устанавливается вместо самого пароля (для безопасности)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class AccountPatchSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    patronymic = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'surname',
            'patronymic',
            'phone',
            'avatar',
            'birthday',
        )
        read_only_fields = ('username',)
        extra_kwargs = {
            'lang': {'write_only': True},
        }

    @staticmethod
    def validate_phone(value):
        if User.objects.filter(phone=value).exists():
            raise CustomValidationError({'phone': 'Номер телефона занят другим пользователем'})

        phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
        if not phone_pattern.match(value):
            raise CustomValidationError({'phone': 'Введён некорректный номер телефона'})

        return value

    def update(self, instance, validated_data):
        updated_instance = super(AccountPatchSerializer, self).update(instance, validated_data)
        return updated_instance

    def get_avatar(self, instance):
        request = self.context.get('request')
        if instance.avatar:
            # Получение пути к изображению
            image_path = instance.avatar.url
            # Построение полного абсолютного пути к изображению
            return request.build_absolute_uri(image_path)
        else:
            return None


class AccountDetailSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    def get_avatar(self, obj):
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        return None

    class Meta:
        model = User
        fields = (
            'email', 'username', 'first_name', 'surname', 'patronymic', 'phone', 'avatar', 'birthday'
        )


class ChangePasswordSerializer(serializers.Serializer):
    pvc = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    verified_password = serializers.CharField(write_only=True)
    message = serializers.JSONField(read_only=True)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise CustomValidationError({'email': 'Не привязана почта к пользователю'})
        return value

    @staticmethod
    def validate_password(value):
        if not validate_password(value)[0] == True:
            raise CustomValidationError({'password': validate_password(value)[1]})

        return value

    def validate(self, data):
        if not UserPvc.objects.filter(email=data['email'], pvc=data['pvc']).exists():
            raise CustomValidationError({'pvc': 'Неверный код'})
        if not data['password'] == data['verified_password']:
            raise CustomValidationError({'password': 'Пароли не совпадают'})
        return data

    def create(self, validated_data):
        UserPvc.objects.filter(email=validated_data.get('email'), pvc=validated_data.get('pvc')).delete()
        user = User.objects.get(email=validated_data.get('email'))
        user.set_password(validated_data['password'])
        user.save()
        return {'message': 'Пароль изменён'}


class CheckEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPvc
        fields = ['email']

    def validate_email(self, value):
        place = self.context['request'].query_params.get('place')   # получение значения параметра `place`
        if not place:
            raise CustomValidationError({'place': 'Не заданы параметры запроса: Выберите один - регистрация, '
                                                  'изменения пароля'})
        if not place in ('register', 'change_password'):
            raise CustomValidationError({'place': 'Ошибка в параметрах запроса'})
        if User.objects.filter(email=value).exists() and place == 'register':
            raise CustomValidationError({'email': 'Почта занята другим пользователем'})
        if not User.objects.filter(email=value).exists() and place == 'change_password':
            raise CustomValidationError({'email': 'Почта не найдена'})
        return value

    def create(self, validated_data):
        instance: UserPvc = super().create(validated_data)
        # Отправка 6-ти значного кода на почту
        instance.send_pvc()
        return instance

    def update(self, instance, validated_data):
        instance: UserPvc = super().update(instance, validated_data)
        instance.send_pvc()
        return instance


class UserAvatarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar',)