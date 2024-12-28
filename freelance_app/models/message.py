from django.db import models
from django.utils import timezone
from freelance_app.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return f'{self.sender.username} -> {self.recipient.username}: {self.subject}'
