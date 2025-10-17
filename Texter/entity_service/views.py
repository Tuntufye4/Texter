from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EntityRecord
from .serializers import EntityRecordSerializer
from .entity_utils import extract_entities

class EntityView(APIView):
    def post(self, request):
        text = request.data.get('text')
        if not text:
            return Response({'error': 'Text required'}, status=status.HTTP_400_BAD_REQUEST)
        data = extract_entities(text)
        record = EntityRecord.objects.create(text=text, entities=data)
        return Response(EntityRecordSerializer(record).data, status=status.HTTP_201_CREATED)
