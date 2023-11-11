import json
import re
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import ChatRoom, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']  # get current user
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    def is_valid_message(self, message):
        """
        Validate the message content.
        For example, you can check if the message contains only alphanumeric characters.
        Modify this function as needed for your specific validation rules.
        """
        # Example: Allow only alphanumeric characters and spaces
        return bool(re.match(r'^[a-zA-Z0-9\s]*$', message))
    # Receive message from WebSocket
    async def receive(self, text_data):
        self.user = self.scope['user']  # get current user
        print(f"self user = {self.user}")
        data = json.loads(text_data)
        print(data)
        message = data['message']
        email = data['email']
        room = data['room']
        # Validate the message
        if not self.is_valid_message(message):
            # Handle invalid message here (e.g., send an error message)
            print("error")
            await self.send(text_data=json.dumps({
                'error': 'Invalid message content',
            }))
            return
        await self.save_message(email , room, message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'email': str(self.user )
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        email = event['email']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'email': email
        }))

    @sync_to_async
    def save_message(self, email, room, message):
        user = User.objects.get(email=email)
        room_obj = ChatRoom.objects.get(pk=room)
        Message.objects.create(user=user, room=room_obj, content=message)