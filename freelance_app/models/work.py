from django.db import models
from .user import User


class BaseService(models.Model):
    SERVICE_TYPES = [
        ('web_development', 'Веб разработка'),
        ('marketing', 'Маркетинг'),
        ('copywriting', 'Копирайтинг'),
        ('rewriting', 'Рерайтинг'),
        ('translations', 'Переводы'),
        ('video_editing', 'Видеомонтаж'),
        ('photo', 'Фотография'),
    ]

    service_type = models.CharField(choices=SERVICE_TYPES, default='web_development', max_length=50)
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
        return f"{super().__str__()}, {self.get_service_type_display()}"

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


class Tag(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
