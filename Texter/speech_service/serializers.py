from rest_framework import serializers
from .models import SpeechRecord

class SpeechRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeechRecord
        fields = '__all__'
   