from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'sender_name', 'conversation', 'message_body', 'sent_at']

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)
    messages = serializers.SerializerMethodField()

    def get_messages(self, obj):
        messages = obj.messages.all().order_by('-sent_at')
        return MessageSerializer(messages, many=True).data

    def validate(self, data):
        participants = data.get('participants', [])
        if len(participants) < 2:
            raise serializers.ValidationError("A conversation must have at least two participants.")
        return data

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']
