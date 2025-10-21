from django.db import models

class TopicRecord(models.Model):
    text = models.TextField()
    topics = models.TextField()  # store topic list or dictionary
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TopicRecord #{self.id}"
