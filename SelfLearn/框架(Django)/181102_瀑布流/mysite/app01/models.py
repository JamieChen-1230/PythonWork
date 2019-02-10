from django.db import models


class Img(models.Model):
    src = models.FileField(max_length=32, verbose_name="圖片路徑", upload_to="static/upload")
    title = models.CharField(max_length=16, verbose_name="標題")
    summary = models.CharField(max_length=128, verbose_name="簡介")
    
    class Meta:
        verbose_name_plural = "圖片"
    
    def __str__(self):
        return self.title
