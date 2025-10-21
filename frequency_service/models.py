from django.db import models

class FrequencyRecord(models.Model):
    text = models.TextField()
    frequencies = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
