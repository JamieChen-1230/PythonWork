from rest_framework import serializers
from nba import models


# Serializers 序列化 是 DRF 很重要的一個地方
# 主要功能是將 Python 結構序列化為其他格式，例如我們常用的 JSON
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        # 設定序列化要使用的參數
        fields = '__all__'  # 代表全部參數
