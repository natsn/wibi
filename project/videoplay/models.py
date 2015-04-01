from django.db import models
from django.contrib.auth.models import User

class VideoUpload(models.Model):
    user = models.ForeignKey(User)
    video = models.FileField(upload_to='video_uploads')
    created_at = models.DateTimeField(auto_now=True)

class Note(models.Model):
    user = models.ForeignKey(User)
    video = models.ForeignKey(VideoUpload)
    mark = models.IntegerField()
    comment = models.CharField(max_length=255)
