from django.db import models


class News(models.Model):
    title = models.CharField(max_length=40)
    outline = models.TextField()
    url = models.URLField()
    img_url = models.URLField()
    content = models.TextField()
    post_date = models.CharField(max_length=30)
    video_url = models.URLField()

    class Meta:
        db_table = "news"
