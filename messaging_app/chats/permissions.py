from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to allow only participants of a conversation to view, update, or delete messages.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the request user is a participant of the conversation
        return request.user in obj.participants.all()
