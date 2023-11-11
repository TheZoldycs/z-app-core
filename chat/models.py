import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ChatRoom(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, verbose_name=("user male"), on_delete=models.CASCADE,blank=True, null=True,related_name="male_chat")
    def __str__(self):
        return self.name
class Message(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.user.email} ({self.timestamp}): {self.content}'

 