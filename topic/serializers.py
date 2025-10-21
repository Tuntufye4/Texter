from rest_framework import serializers
from .models import TopicRecord

class TopicRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicRecord
        fields = "__all__"
      