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
            return Response('Text required', status=status.HTTP_400_BAD_REQUEST)
        
        # Generate summary
        summary_text = summarize_text(text, count)   
        
        # Save record
        record = SummaryRecord.objects.create(text=text, summary=summary_text)
        
        # Return summary as plain text
        return Response(summary_text, content_type='text/plain', status=status.HTTP_201_CREATED)

    def get(self, request):
        """  
        List all summarized records.
        """
        records = SummaryRecord.objects.all().order_by('-created_at')  # newest first
        serializer = SummaryRecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
