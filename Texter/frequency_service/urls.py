from django.urls import path
from .views import FrequencyView

urlpatterns = [
    path('frequency/', FrequencyView.as_view(), name='word_frequency'),
]
