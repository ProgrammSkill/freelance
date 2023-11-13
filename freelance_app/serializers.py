from rest_framework import serializers

from freelance_app import models
from freelance_app.models import User, Executor, Customer, Service, Order, Tag, Ordering, Message, Ticket, Review, \
    Authoring


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'phone', 'name', 'surname', 'lastname', 'birthday', 'photo']


class ExecutorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        models = Executor
        fields = '__all__'


class CreateExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        models = Executor
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        models = Customer
        fields = '__all__'


class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        models = Customer
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()
    service_type = serializers.CharField(source='get_service_type__display')

    class Meta:
        models = Service
        fields = '__all__'


class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        models = Service
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    executor = CustomerSerializer()
    order_type = serializers.CharField(source='get_order_type_display')

    class Meta:
        models = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        models = Order
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    order = OrderSerializer()

    class Meta:
        models = Tag
        fields = '__all__'


class CreateTagSerializer(serializers.ModelSerializer):
    class Meta:
        models = Tag
        fields = '__all__'


class OrderingSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    order = OrderSerializer()
    customer = CustomerSerializer()
    executor = ExecutorSerializer()

    class Meta:
        models = Ordering
        fields = '__all__'


class OrderingTagSerializer(serializers.ModelSerializer):
    class Meta:
        models = Ordering
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    executor = ExecutorSerializer()

    class Meta:
        models = Message
        fields = '__all__'


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        models = Message
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    executor = ExecutorSerializer()
    severity = serializers.CharField(source='get_severity_display')

    class Meta:
        models = Ticket
        fields = '__all__'


class CreateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        models = Ticket
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    ticket_type = serializers.CharField(source='get_rating_display')

    class Meta:
        models = Review
        fields = '__all__'


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        models = Review
        fields = '__all__'


class AuthoringSerializer(serializers.ModelSerializer):
    review = ReviewSerializer()
    author = UserSerializer()
    customer = CustomerSerializer()
    executor = ExecutorSerializer()

    class Meta:
        models = Authoring
        fields = '__all__'


class CreateAuthoringSerializer(serializers.ModelSerializer):
    class Meta:
        models = Authoring
        fields = '__all__'