from rest_framework import serializers
from django.contrib.auth import get_user_model
from meetings.models import Meetings
User = get_user_model()


class MeetingSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)
    class Meta:
        model = Meetings
        fields = ('topic', 'duration','starttime','passwords','url')

   
