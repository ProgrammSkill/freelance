from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from freelance_app.common_utils.pvc import get_random_integer, send_email


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    surname = models.CharField(max_length=150, blank=True, null=True)
    patronymic = models.CharField(max_length=150, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False, null=True)
    is_superuser = models.BooleanField(default=0, null=True)
    is_active = models.BooleanField(default=1, null=True)
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    @property
    def fullname(self):
        return f'{self.name} {self.patronymic}'


class UserOutstandingToken(OutstandingToken):
    DEVICES_IDS = [
        [0, "Desktop"],
        [1, "Android"],
        [2, "iOS"],
        [3, "Mobile WEB"],
        [4, "DWED infomat"],
        [5, "TMED"],
    ]

    device_id = models.IntegerField(choices=DEVICES_IDS, default=0)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    mac_address = models.CharField(max_length=128, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, to_field='username')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'token_blacklist_outstandingtoken'


def generate_pvc():
    return get_random_integer(6)


class UserPvc(models.Model):
    """ Модель для хранения генерируемого кода для определённой почты при регистрации или изменения пароля """
    email = models.CharField(unique=True, max_length=255)
    pvc = models.CharField(max_length=10, default=generate_pvc)

    def send_pvc(self):
        self.pvc = generate_pvc()
        send_email(self.email, 'Код подтверждения для Фриланс Биржи', self.pvc)
        self.save()