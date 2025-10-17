from rest_framework import serializers
from .models import EntityRecord

class EntityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityRecord
        fields = '__all__'
