from django.db import models
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .user import User


class Service(models.Model):
    SERVICE_TYPES = [
        ('1', 'Веб разработка'),
        ('2', 'Маркетинг'),
        ('3', 'Копирайтинг'),
        ('4', 'Рерайтинг'),
        ('5', 'Переводы'),
        ('6', 'Видеомонтаж'),
        ('7', 'Фотография'),
    ]

    executor = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desk = models.CharField(max_length=1000)
    price = models.IntegerField()
    service_type = models.CharField(choices=SERVICE_TYPES, default='1', max_length=1)

    def __str__(self):
        return f"{self.name}, {self.get_service_type_display()}, price: {self.price}"

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'


class Order(models.Model):
    ORDER_TYPES = [
        ('1', 'Веб разработка'),
        ('2', 'Маркетинг'),
        ('3', 'Копирайтинг'),
        ('4', 'Рерайтинг'),
        ('5', 'Переводы'),
        ('6', 'Видеомонтаж'),
        ('7', 'Фотография'),
    ]

    customer = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desk = models.CharField(max_length=1000)
    price = models.IntegerField()
    order_type = models.CharField(choices=ORDER_TYPES, default='1', max_length=1)

    def __str__(self):
        return f"{self.name}, {self.get_order_type_display()}, price: {self.price}"

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'