from django.urls import path
from .views import TopicModelingView

urlpatterns = [
    path('topic/', TopicModelingView.as_view(), name='topic_modeling'),
]
      