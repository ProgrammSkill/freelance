from rest_framework import serializers
from freelance_app.models.work import Service, Order


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
