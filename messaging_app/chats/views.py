from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        participants = request.data.get('participants', [])
        if len(participants) < 2:
            return Response({"error": "At least two participants are required."}, status=400)
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        return Response(ConversationSerializer(conversation).data)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        sender_id = request.data.get('sender')
        conversation_id = request.data.get('conversation')
        message_body = request.data.get('message_body')

        message = Message.objects.create(
            sender_id=sender_id,
            conversation_id=conversation_id,
            message_body=message_body,
        )
        return Response(MessageSerializer(message).data)

