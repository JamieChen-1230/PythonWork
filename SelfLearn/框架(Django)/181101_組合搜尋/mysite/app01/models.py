from django.db import models


class Direction(models.Model):
    """
    方向： 自動化、測試、運維、前端
    """
    name = models.CharField(verbose_name="名稱", max_length=32)
    classification = models.ManyToManyField("Classification")

    class Meta:
        db_table = "Direction"
        verbose_name_plural = "方向(視頻方向)"

    def __str__(self):
        return self.name


class Classification(models.Model):
    """
    分類： Python,  Linux, JavaScript, OpenStack, Node.js
    """
    name = models.CharField(verbose_name="名稱", max_length=32)

    class Meta:
        db_table = "Classification"
        verbose_name_plural = "分類(視頻分類)"

    def __str__(self):
        return self.name


class Level(models.Model):
    title = models.CharField(max_length=32)

    class Meta:
        db_table = "Level"
        verbose_name_plural = "難度級別"

    def __str__(self):
        return self.title


class Video(models.Model):
    status_choice = (
        (1, "下線"),
        (2, "上線"),
    )

    status = models.IntegerField(verbose_name="狀態", choices=status_choice, default=2)
    level = models.ForeignKey("Level")
    classification = models.ForeignKey("Classification", null=True, blank=True)

    weight = models.IntegerField(verbose_name="權重", default=0)

    title = models.CharField(verbose_name="標題", max_length=32)
    summary = models.CharField(verbose_name="簡介", max_length=32)
    # img = models.ImageField(verbose_name="圖片", upload_to="./static/images/Video/")
    img = models.CharField(verbose_name="圖片", max_length=32)
    href = models.CharField(verbose_name="視頻地址", max_length=256)

    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Video"
        verbose_name_plural = "視頻"

    def __str__(self):
        return self.title
