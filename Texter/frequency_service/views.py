from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FrequencyRecord
from .serializers import FrequencyRecordSerializer
from .freq_utils import word_frequency

class FrequencyView(APIView):
    def post(self, request):
        text = request.data.get('text')
        if not text:
            return Response({'error': 'Text required'}, status=status.HTTP_400_BAD_REQUEST)
        data = word_frequency(text)
        record = FrequencyRecord.objects.create(text=text, frequencies=data)
        return Response(FrequencyRecordSerializer(record).data, status=status.HTTP_201_CREATED)
