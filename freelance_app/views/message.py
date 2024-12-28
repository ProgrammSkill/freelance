from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Message
from ..models import User
from ..serializers.messsage import MessageSerializer


class MessageCreateAPIView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        sender = self.request.user
        recipient_id = self.request.data.get('recipient_id')
        recipient = User.objects.get(id=recipient_id)
        serializer.save(sender=sender, recipient=recipient)