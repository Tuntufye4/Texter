from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TopicRecord
from .serializers import TopicRecordSerializer
from .topic_utils import extract_topics

class TopicModelingView(APIView):
    def post(self, request):
        text = request.data.get('text')
        n_topics = int(request.data.get('n_topics', 5))
        if not text:
            return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)

        topics = extract_topics(text, n_topics)
        record = TopicRecord.objects.create(text=text, topics=topics)
        return Response(TopicRecordSerializer(record).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        records = TopicRecord.objects.all().order_by('-created_at')
        serializer = TopicRecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
