from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Message, Notification

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def log_message_edits(sender, instance, **kwargs):
    if instance.pk:  # Check if the message already exists (not a new instance)
        try:
            # Get the existing message content
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:  # Content has changed
                # Save the old content in MessageHistory
                MessageHistory.objects.create(
                    message=old_message,
                    old_content=old_message.content
                )
                # Mark the message as edited
                instance.edited = True
        except Message.DoesNotExist:
            pass
