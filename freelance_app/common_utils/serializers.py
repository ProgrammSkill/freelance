from rest_framework import serializers
from rest_framework_simplejwt.settings import api_settings
from freelance_app.common_utils.file_paths import get_absolute_media_url_from_field
from freelance_app.common_utils.token import get_token_class


# Класс позволяет преобразовать значение поля в представление.
class CharToStorageField(serializers.CharField):

    def to_representation(self, value):
        if not value:
            return None
        if value.startswith('http://') or value.startswith('https://'):
            return value
        return get_absolute_media_url_from_field(value)


class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField(read_only=True)

    def token_class(self):
        return get_token_class(self.context['request'])

    def validate(self, attrs):
        refresh = self.token_class()(attrs["refresh"])

        data = {"access": str(refresh.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Попытка занести данный токен обновления в черный список
                    refresh.blacklist()
                except AttributeError:
                    # Если приложение blacklist не установлено, метод `черный список` будет
                    # отсутствовать
                    pass

            refresh.set_jti()
            refresh.set_exp()
            refresh.set_iat()

            data["refresh"] = str(refresh)

        return data