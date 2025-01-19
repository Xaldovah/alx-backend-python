from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['participants__username']
    ordering_fields = ['created_at']

    def create(self, request, *args, **kwargs):
        participants = request.data.get('participants', [])
        if len(participants) < 2:
            raise serializers.ValidationError("A conversation must have at least two participants.")
        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        return Response(ConversationSerializer(conversation).data)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['sent_at']

    def create(self, request, *args, **kwargs):
        sender = request.user
        conversation_id = request.data.get('conversation')
        message_body = request.data.get('message_body')

        if not conversation_id or not message_body:
            raise serializers.ValidationError("Both 'conversation' and 'message_body' fields are required.")

        message = Message.objects.create(
            sender=sender,
            conversation_id=conversation_id,
            message_body=message_body
        )
        return Response(MessageSerializer(message).data)
