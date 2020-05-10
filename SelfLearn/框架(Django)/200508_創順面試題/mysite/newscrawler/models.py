from django.db import models


class News(models.Model):
    title = models.CharField(max_length=40)
    outline = models.TextField()
    hour_ago = models.CharField(max_length=20)
    url = models.URLField()
    img_url = models.URLField()
    content = models.ForeignKey("Contents")


class Contents(models.Model):
    content = models.TextField()
    upload_time = models.CharField(max_length=30)
    video_url = models.URLField()

