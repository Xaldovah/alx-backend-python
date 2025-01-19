from django_filters import rest_framework as filters
from .models import Message

class MessageFilter(filters.FilterSet):
    min_date = filters.DateTimeFilter(field_name="sent_at", lookup_expr="gte")
    max_date = filters.DateTimeFilter(field_name="sent_at", lookup_expr="lte")
    sender = filters.CharFilter(field_name="sender__username", lookup_expr="icontains")

    class Meta:
        model = Message
        fields = ['min_date', 'max_date', 'sender']
