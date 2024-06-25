from django.db import models
from .user import User


class BaseService(models.Model):
    SERVICE_TYPES = [
        ('1', 'Веб разработка'),
        ('2', 'Маркетинг'),
        ('3', 'Копирайтинг'),
        ('4', 'Рерайтинг'),
        ('5', 'Переводы'),
        ('6', 'Видеомонтаж'),
        ('7', 'Фотография'),
    ]

    service_type = models.CharField(choices=SERVICE_TYPES, default='1', max_length=1)
    name = models.CharField(max_length=250)
    desk = models.CharField(max_length=1000)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}, price: {self.price}"

    class Meta:
        abstract = True

class Service(BaseService):
    executor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{super().__str__()}, {self.get_service_type_display()}"

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

class Order(BaseService):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{super().__str__()}, {self.get_order_type_display()}"

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
