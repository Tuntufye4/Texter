from rest_framework import serializers
from .models import SummaryRecord

class SummaryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryRecord
        fields = '__all__'
