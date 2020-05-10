from django.shortcuts import render
from django.shortcuts import get_object_or_404
from musics.models import Music
from musics.serializers import MusicSerializer
from rest_framework.response import Response
# 在DRF中較常使用viewsets
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route


# 只需要寫這樣，你就擁有 CRUD 的全部功能，當然，如果你需要，也可以覆寫他。
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()  # 找出所有music數據
    serializer_class = MusicSerializer  # 序列化類
    # permission_classes = (IsAuthenticated,)  # 權限，可以python manage.py createsuperuser來使用

    # 如果你沒有額外指定，通常你的 url_path 就是你 function 命名的名稱
    # URL pattern: /api/music/{pk}/{url_path}/
    @detail_route(methods=['get'], url_path="detail_self")
    def detail(self, request, pk=None):
        music = get_object_or_404(Music, pk=pk)
        result = {
            'singer': music.singer,
            'song': music.song
        }

        return Response(result, status=status.HTTP_200_OK)

    # 如果你沒有額外指定，通常你的 url_path 就是你 function 命名的名稱
    # URL pattern: /api/music/{url_path}/
    @list_route(methods=['get'])
    def all_singer(self, request):
        music = Music.objects.values_list('singer', flat=True).distinct()
        return Response(music, status=status.HTTP_200_OK)


def index(request):
    return render(request, "index.html", {})
