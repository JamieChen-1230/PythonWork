from django.db import models


class User(models.Model):
    """
    用戶表
    """
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    # m = models.ManyToManyField("Role")

    class Meta:
        verbose_name_plural = '用戶表'

    def __str__(self):
        return self.username


class Role(models.Model):
    """
    角色表
    """
    caption = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = '角色表'

    def __str__(self):
        return self.caption


class User2Role(models.Model):
    """
    用戶角色關係表
    """
    u = models.ForeignKey(User)
    r = models.ForeignKey(Role)

    class Meta:
        verbose_name_plural = '用戶分配角色'

    def __str__(self):
        return "%s-%s" % (self.u.username, self.r.caption,)


class Action(models.Model):
    """
    操作表:
    get      代表獲取信息 (1)
    post     代表創建信息 (2)
    delete  代表刪除信息 (3)
    put      代表修改信息 (4)
    """
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)  # 關鍵字

    class Meta:
        verbose_name_plural = '操作表'

    def __str__(self):
        return self.caption


class Menu(models.Model):
    """
    1    菜單1        null
    2    菜單2        null
    3    菜單3        null
    4    菜單1.1       1
    5    菜單1.2       1
    6    菜單1.2.1    4
    這樣菜單無最後一層，直到放權限為止
    """
    caption = models.CharField(max_length=32)
    parent = models.ForeignKey('self', related_name='p', null=True, blank=True)

    class Meta:
        verbose_name_plural = '菜單表'

    def __str__(self):
        return "%s" % (self.caption,)


class Permission(models.Model):
    """
    URL表:
    http://127.0.0.1:8001/user.html  代表用戶管理 (1)
        -- http://127.0.0.1:8001/user.html?t=get  代表獲取用戶信息
        -- http://127.0.0.1:8001/user.html?t=post  代表創建用戶信息
        -- http://127.0.0.1:8001/user.html?t=delete  代表刪除用戶信息
        -- http://127.0.0.1:8001/user.html?t=put  代表修改用戶信息
    http://127.0.0.1:8001/order.html 代表訂單管理 (2)
    """
    caption = models.CharField(max_length=32)
    url = models.CharField(max_length=32)
    menu = models.ForeignKey(Menu, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'URL表'

    def __str__(self):
        return "%s-%s" % (self.caption, self.url,)


class Permission2Action(models.Model):
    """
    權限表(url+操作):
    (1) + (1)  => 代表獲取用戶信息
    (1) + (2)  => 代表創建用戶信息
    (1) + (3)  => 代表刪除用戶信息
    (2) + (1)  => 代表獲取訂單信息
    ...
    """
    p = models.ForeignKey(Permission)
    a = models.ForeignKey(Action)

    class Meta:
        verbose_name_plural = '權限表'

    def __str__(self):
        return "%s-%s:-%s?t=%s" % (self.p.caption, self.a.caption, self.p.url, self.a.code,)


class Permission2Action2Role(models.Model):
    """
    角色權限關係表
    """
    p2a = models.ForeignKey(Permission2Action)
    r = models.ForeignKey(Role)

    class Meta:
        verbose_name_plural = '角色分配權限'

    def __str__(self):
        return "%s==>%s" % (self.r.caption, self.p2a,)

