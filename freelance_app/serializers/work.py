from rest_framework import serializers
from freelance_app.models.work import Service, Order, Tag


class ServiceSerializer(serializers.ModelSerializer):
    service_type = serializers.ChoiceField(choices=Service.SERVICE_TYPES)
    executor = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Service
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    service_type = serializers.ChoiceField(choices=Order.SERVICE_TYPES)
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = '__all__'


class TagListSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    order = OrderSerializer()

    class Meta:
        model = Tag
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
