from rest_framework import serializers
from .models import Message
from rest_framework import serializers
from freelance_app.models.message import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'recipient', 'subject', 'body', 'timestamp', 'read')