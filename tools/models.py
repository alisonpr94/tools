from django.db import models

class Tool(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()
    tags = models.JSONField()