from django.db import models


class UserInfo(models.Model):
    """
    用戶表
    """
    nid = models.BigAutoField(primary_key=True)  # 主鍵
    username = models.CharField(verbose_name='用戶名', max_length=32, unique=True)  # 用戶名不可重複
    password = models.CharField(verbose_name='密碼', max_length=64)
    nickname = models.CharField(verbose_name='暱稱', max_length=32)
    email = models.EmailField(verbose_name='信箱', unique=True)  # 信箱不可重複
    avatar = models.ImageField(verbose_name='頭像', null=True)
    create_time = models.DateTimeField(verbose_name='創建時間', auto_now_add=True)

    fans = models.ManyToManyField(verbose_name='粉絲表',
                                  to='UserInfo',  # 自關聯
                                  through='UserFans',  # 手動指定中間表
                                  related_name='f',
                                  through_fields=('user', 'follower'))

    def __str__(self):
        return self.username


class Blog(models.Model):
    """
    博客表
    """
    nid = models.BigAutoField(primary_key=True)  # 主鍵索引
    title = models.CharField(verbose_name='個人博客標題', max_length=64)
    site = models.CharField(verbose_name='個人博客前綴名', max_length=32, unique=True)  # 前綴名不可重複(唯一索引)
    theme = models.CharField(verbose_name='博客主題', max_length=32)
    user = models.OneToOneField(to='UserInfo', to_field='nid')  # 跟用戶表為一對一關係

    def __str__(self):
        return self.title


class UserFans(models.Model):
    """
    互粉表
    """
    user = models.ForeignKey(verbose_name='版主', to='UserInfo', to_field='nid', related_name='users')
    follower = models.ForeignKey(verbose_name='粉絲', to='UserInfo', to_field='nid', related_name='followers')

    class Meta:
        # 聯合唯一
        unique_together = [
            ('user', 'follower'),
        ]


class Category(models.Model):
    """
    博客個人文章分類表
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分類標題', max_length=32)
    # 跟博客成多對一關聯，而不是跟用戶表，因為用戶不一定有博客
    blog = models.ForeignKey(verbose_name='所屬博客', to='Blog', to_field='nid')
    # blog_id

    def __str__(self):
        return self.title


class ArticleDetail(models.Model):
    """
    文章詳細表
    """
    content = models.TextField(verbose_name='文章内容', )
    # 跟文章表成一對一關係
    article = models.OneToOneField(verbose_name='所屬文章', to='Article', to_field='nid')


class UpDown(models.Model):
    """
    踩頂表
    """
    article = models.ForeignKey(verbose_name='文章', to='Article', to_field='nid')
    user = models.ForeignKey(verbose_name='用戶', to='UserInfo', to_field='nid')
    up = models.BooleanField(verbose_name='是否頂')

    class Meta:
        # 因為不是頂就是踩，具唯一性
        unique_together = [
            ('article', 'user'),
        ]


class Comment(models.Model):
    """
    評論表
    """
    nid = models.BigAutoField(primary_key=True)
    content = models.CharField(verbose_name='内容', max_length=255)
    create_time = models.DateTimeField(verbose_name='創建時間', auto_now_add=True)

    reply = models.ForeignKey(verbose_name='回覆評論', to='self', related_name='back', null=True)  # 自關聯
    article = models.ForeignKey(verbose_name='評論文章', to='Article', to_field='nid')
    user = models.ForeignKey(verbose_name='評論者', to='UserInfo', to_field='nid')

    def __str__(self):
        return self.content

class Tag(models.Model):
    """
    博客個人文章標籤表
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='標籤名', max_length=32)

    blog = models.ForeignKey(verbose_name='所屬博客', to='Blog', to_field='nid')
    # blog_id

    def __str__(self):
        return self.title


class Article(models.Model):
    """
    文章表
    """
    nid = models.BigAutoField(primary_key=True)
    title = models.CharField(verbose_name='文章標題', max_length=128)
    summary = models.CharField(verbose_name='文章簡介', max_length=255)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)
    create_time = models.DateTimeField(verbose_name='創建時間', auto_now_add=True)

    blog = models.ForeignKey(verbose_name='所屬博客', to='Blog', to_field='nid')
    category = models.ForeignKey(verbose_name='文章類型', to='Category', to_field='nid', null=True)

    # 內建分類
    type_choices = [
        (1, "Python"),
        (2, "Linux"),
        (3, "OpenStack"),
        (4, "GoLang"),
    ]
    # 1,2,3,4
    article_type_id = models.IntegerField(choices=type_choices, default=None)

    tags = models.ManyToManyField(
        to="Tag",
        through='Article2Tag',  # 手動指定中間表
        through_fields=('article', 'tag'),
    )

    def __str__(self):
        return self.title


class Article2Tag(models.Model):
    article = models.ForeignKey(verbose_name='文章', to="Article", to_field='nid')
    tag = models.ForeignKey(verbose_name='標籤', to="Tag", to_field='nid')

    class Meta:
        # 聯合唯一
        unique_together = [
            ('article', 'tag'),
        ]


# ----------------------報障單----------------------
class Trouble(models.Model):
    title = models.CharField(max_length=32)
    detail = models.TextField()
    user = models.ForeignKey(UserInfo, related_name="u")  # 提交者
    # create_time = models.CharField(max_length=32)  # 希望存的格式是秒的那種 ex:148252656.265656
    create_time = models.DateTimeField()

    status_choices = (
        (1, "未處理"),
        (2, "處理中"),
        (3, "已處理"),
    )
    status = models.IntegerField(choices=status_choices, default=1)

    processor = models.ForeignKey(UserInfo, related_name="p", null=True, blank=True)  # 解決者
    solution = models.TextField(null=True, blank=True)
    solution_time = models.DateTimeField(null=True, blank=True)

    pj_choices = (
        (1, "不滿意"),
        (2, "一般"),
        (3, "粉滿意"),
    )
    pj = models.IntegerField(choices=pj_choices, default=2, null=True, blank=True)  # 評價
