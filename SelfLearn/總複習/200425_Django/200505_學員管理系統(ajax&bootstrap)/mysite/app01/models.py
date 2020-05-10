from django.db import models


class Classes(models.Model):
    """
    班級表
    """
    name = models.CharField(max_length=32)
    ct = models.ManyToManyField('Teachers', related_name='classes_set')

    def __str__(self):
        return self.name


class Teachers(models.Model):
    """
    老師表
    """
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Students(models.Model):
    """
    學生表
    id, name, age, gender, cs_id
    """
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey('Classes')

    def __str__(self):
        return self.name
