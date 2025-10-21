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

    def get(self, request):
        """
        List all entity records.
        """
        records = EntityRecord.objects.all().order_by('-created_at')  # optional: newest first
        serializer = EntityRecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  