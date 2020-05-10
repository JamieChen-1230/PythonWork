from rest_framework import serializers
from musics.models import Music


# 序列化
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music  # 要序列化的表

        # 設定序列化要使用的參數
        # fields = '__all__' 代表全部參數
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')
