from django.urls import path
from .views import EntityView

urlpatterns = [
    path('entities/', EntityView.as_view(), name='entities'),
]
