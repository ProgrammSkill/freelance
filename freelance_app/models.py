from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20,  unique=True)
    password = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150, blank=True, null=True)
    lastname = models.CharField(max_length=150)
    birthday = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="photos/", null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=0, null=True)
    is_active = models.BooleanField(default=1, null=True)

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    @property
    def fullname(self):
        return f'{self.name} {self.lastname}'


class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user}"

    class Meta:
        verbose_name = 'Исполнители'
        verbose_name_plural = 'Исполнители'


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user}"

    class Meta:
        verbose_name = 'Заказчики'
        verbose_name_plural = 'Заказчики'


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

    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
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

    customer = models.ForeignKey(Executor, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desk = models.CharField(max_length=1000)
    price = models.IntegerField()
    order_type = models.CharField(choices=ORDER_TYPES, default='1', max_length=1)

    def __str__(self):
        return f"{self.name}, {self.get_order_type_display()}, price: {self.price}"

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


class Tag(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)

class Ordering(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.order_date} - {self.deadline}, Customer: {self.customer}, Executor: {self.executor}"

    class Meta:
        verbose_name = 'Оформленные заказы'
        verbose_name_plural = 'Оформленные заказы'

class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    msg_date = models.DateTimeField()
    is_edited = models.BooleanField()
    desc = models.CharField(max_length=1000)


class Ticket(models.Model):
    SEVERITIES = [
        ('1', 'Низкая'),
        ('2', 'Средняя'),
        ('3', 'Высокая')
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    severity = models.CharField(choices=SEVERITIES, default='1', max_length=1)
    desc = models.CharField(max_length=1000)
    ticket_date = models.DateTimeField()
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.get_severity_display()} {self.ticket_date}, Is resolved {self.is_resolved}'


class Review(models.Model):
    RETING_FIELD = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '6')
    ]

    rating = models.CharField(choices=RETING_FIELD, default='1', max_length=1)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.get_rating_display()}'


class Authoring(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    review_date = models.DateTimeField()

    def __str__(self):
        return f"{self.author}, {self.review_date}"
