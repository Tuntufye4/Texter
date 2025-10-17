from django.db import models

class EntityRecord(models.Model):
    text = models.TextField()
    entities = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
