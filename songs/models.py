from django.db import models

class Song(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    trackID = models.CharField(max_length=100, blank=True, default='')
    indexID = models.IntegerField(blank=False, default=0)
    startPosition = models.IntegerField(blank=False, default=0)

    class Meta:
        ordering = ('created',)