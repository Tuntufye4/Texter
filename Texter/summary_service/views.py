from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SummaryRecord
from .serializers import SummaryRecordSerializer
from .summary_utils import summarize_text

class SummarizeView(APIView):
    def post(self, request):
        text = request.data.get('text')
        count = int(request.data.get('sentences_count', 3))
        if not text:
            return Response({'error': 'Text required'}, status=status.HTTP_400_BAD_REQUEST)
        data = summarize_text(text, count)
        record = SummaryRecord.objects.create(text=text, summary=data)
        return Response(SummaryRecordSerializer(record).data, status=status.HTTP_201_CREATED)
