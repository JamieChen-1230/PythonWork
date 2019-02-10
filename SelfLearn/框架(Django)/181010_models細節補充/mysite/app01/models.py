from django.db import models


# ----------------通用參數----------------
class UserInfo(models.Model):
    """
    字段通用參數：
    null                    數據庫中字段是否可以為空
    default                默認值
    db_column         數據庫中字段的列名
    db_index            數據庫中字段是否可以建立索引(增加查詢速度)
    unique                數據庫中字段是否可以建立唯一索引(增加查詢速度、限制唯一值)
    primary_key       數據庫中字段是否為主鍵(增加查詢速度、限制唯一值、不能為空)
    error_messages   自定義錯誤信息（字典類型），從而定制想要顯示的錯誤信息
    validators           自定義錯誤驗證（列表類型），從而定制想要的驗證規則
    verbose_name      Admin中顯示的字段名稱
    blank                   Admin中是否允許用戶輸入為空
    editable               Admin中是否可以編輯
    help_text             Admin中該字段的提示信息
    choices               Admin中顯示選擇框的內容，用不變動的數據放在內存中從而避免跨表操作
    """
    username = models.CharField(
        max_length=32,
        db_index=True,  # 只能加速查找
        verbose_name='用戶名',
        blank=True,
        help_text='請輸入全英文用戶名',
    )

    user_type_choice = [
        (0, '普通用戶'),
        (1, '超級用戶'),
        (2, 'VIP'),
    ]
    user_type = models.IntegerField(
        choices=user_type_choice,
    )


# ----------------內建一對多----------------
class Staff(models.Model):
    """
    特殊參數：
    ForeignKey(一對多)
        to：要進行關聯的表名
        to_field ：要關聯的表中的字段名稱
        on_delete：當刪除關聯表中的數據時，當前表與其關聯的行的行為
              =models.CASCADE，刪除關聯數據，與之關聯也刪除
              =models.DO_NOTHING，刪除關聯數據，引發錯誤IntegrityError
              =models.SET_NULL，刪除關聯數據，與之關聯的值設置為null（前提FK字段需要設置為可空）
              =models.SET_DEFAULT，刪除關聯數據，與之關聯的值設置為默認值（前提FK字段需要設置默認值）
              =models.SET(func)，刪除關聯數據，與之關聯的值設置為func的返回值
        related_name：反向操作時，使用的字段名，用於代替【表名_set】(推薦都加上)
        db_constraint：是否在數據庫中創建外鍵約束
        limit_choices_to：在Admin或ModelForm中顯示關聯數據時，提供的條件

    OneToOneField(一對一 )：繼承ForeignKey並加上唯一索引
    """
    name = models.CharField(max_length=32, db_index=True,)
    par = models.ForeignKey(
        to="Part",
        to_field='id',
        limit_choices_to={'id__gt': 1},  # 只顯示id>1的選項
    )

    def __str__(self):
        return self.name


class Part(models.Model):
    caption = models.CharField(max_length=12)

    def __str__(self):
        return self.caption


# ----------------內建多對多----------------
class Tag(models.Model):
    """
    ManyToManyField(多對多)額外參數
        db_table：默認創建第三張表時，數據庫中表的名稱
    """
    title = models.CharField(max_length=16)
    # 使用ManyToManyField只能在第三表中創建3個字段(本身id, A表id, B表id)
    staf = models.ManyToManyField(
        to="Staff",  # 默認使用主鍵(id)進行管理
    )

    # 自關聯，透過ManyToManyField指向自己
    # self_m = models.ManyToManyField("self")


# ----------------自定義多對多(兩個ForeignKey)----------------
class Staff2(models.Model):
    name = models.CharField(max_length=32, db_index=True,)

    def __str__(self):
        return self.name


class Tag2(models.Model):
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title


class Staff2ToTag2(models.Model):
    nid = models.AutoField(primary_key=True)
    s = models.ForeignKey(to="Staff2")
    t = models.ForeignKey(to="Tag2")
    ctime = models.DateField()

    class Meta:
        # 使用聯合唯一，不然會造成同一個人有同一個外號的數據出現
        unique_together = [
            ('s', 't'),
        ]
