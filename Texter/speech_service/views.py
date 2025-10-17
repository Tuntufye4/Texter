from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SpeechRecord
from .serializers import SpeechRecordSerializer
from .tts_utils import text_to_speech

class TextToSpeechView(APIView):
    def post(self, request):
        text = request.data.get('text')
        rate = request.data.get('rate', None)
        fmt = request.data.get('format', 'wav')
        if not text:
            return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)

        audio = text_to_speech(text, format=fmt, rate=rate)
        record = SpeechRecord.objects.create(text=text, audio_data=audio)
        return Response(SpeechRecordSerializer(record).data, status=status.HTTP_201_CREATED)
   