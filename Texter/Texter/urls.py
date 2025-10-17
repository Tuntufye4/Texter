from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/speech/', include('speech_service.urls')),
    path('api/frequency/', include('frequency_service.urls')),
    path('api/entities/', include('entity_service.urls')),
    path('api/summary/', include('summary_service.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     