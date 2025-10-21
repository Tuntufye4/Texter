from rest_framework import serializers
from .models import FrequencyRecord

class FrequencyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequencyRecord    
        fields = '__all__'
   