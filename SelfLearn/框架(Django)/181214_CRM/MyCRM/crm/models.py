from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

"""
反向查找：
ForeignKey: 表名(小寫)_set
OneToOneField: 表名(小寫)
"""


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """創建一般user，需輸入email, name, password"""
        if not email:  # 設定為必填，並作為帳號
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """創建超級user，需輸入email, name, password"""
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_superuser = True  # 跟一般用戶的區別
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """用戶信息表(員工、講師使用)"""
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=64, verbose_name="姓名")
    role = models.ManyToManyField("Role", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    class Meta:
        # 自定義權限名單
        permissions = (
            ("crm_model_list", "允許訪問kingadmin中crm的model列表"),
            ("crm_table_list", "可以查看kingadmin每張表裡的所有數據"),
            ("crm_table_list_view", "可以訪問kingadmin每條數據的修改頁"),
            ("crm_table_list_change", "可以對kingadmin每條數據進行修改"),
            ("crm_model_obj_add_view", "可以訪問kingadmin每條數據的增加頁"),
            ("crm_model_obj_add", "可以對kingadmin每條數據進行添加"),
            ("crm_view_my_own_customers", "可以查看kingadmin每張表裡的自定義數據"),
        )


class Role(models.Model):
    """角色表"""
    name = models.CharField(max_length=64, unique=True)
    menus = models.ManyToManyField("Menus", blank=True, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    """學員表"""
    customer = models.OneToOneField("CustomerInfo")
    class_grade = models.ManyToManyField("ClassList")

    def __str__(self):
        return "%s" % self.customer


class CustomerInfo(models.Model):
    """客戶信息表"""
    name = models.CharField(max_length=64, default=None)
    contact_type_choices = (
        (0, "qq"),
        (1, "微信"),
        (2, "手機"),
    )
    contact_type = models.SmallIntegerField(choices=contact_type_choices, default=0)
    contact = models.CharField(max_length=64, unique=True)
    source_choices = (
        (0, "QQ群"),
        (1, "51CTO"),
        (2, "百度推廣"),
        (3, "知乎"),
        (4, "轉介紹"),
        (5, "其他"),
    )
    source = models.SmallIntegerField(choices=source_choices)
    referral_from = models.ForeignKey("self", blank=True, null=True, verbose_name="轉介紹者")
    consult_courses = models.ManyToManyField("Course", verbose_name="諮詢課程")
    consult_content = models.TextField(verbose_name="諮詢內容")
    status_choices = (
        (0, "未報名"),
        (1, "已報名"),
        (2, "已退學"),
    )
    status = models.SmallIntegerField(choices=status_choices)
    consultant = models.ForeignKey("UserProfile", verbose_name="顧問")
    id_num = models.CharField(max_length=128, blank=True, null=True)
    emergency_contact = models.PositiveIntegerField(blank=True, null=True)
    sex_choices = (
        (0, "男"),
        (1, "女"),
    )
    sex = models.PositiveSmallIntegerField(choices=sex_choices, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "客戶信息"
        verbose_name_plural = "客戶信息"


class CustomerFollowUp(models.Model):
    """客戶追蹤紀錄表"""
    customer = models.ForeignKey("CustomerInfo")
    content = models.TextField(verbose_name="跟蹤內容")
    user = models.ForeignKey("UserProfile", verbose_name="跟蹤人")
    status_choices = (
        (0, "目前尚未想報名"),
        (1, "一個月內報名"),
        (2, "二周內報名"),
        (3, "已報名"),
    )
    status = models.SmallIntegerField(choices=status_choices)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content


class Course(models.Model):
    """課程表"""
    name = models.CharField(max_length=64, unique=True, verbose_name="課程名稱")
    price = models.PositiveIntegerField()  # 正整數
    period = models.PositiveSmallIntegerField(default=5, verbose_name="課程週期(月)")
    outline = models.TextField(verbose_name="大綱")

    def __str__(self):
        return self.name


class ClassList(models.Model):
    """班級表"""
    branch = models.ForeignKey("Branch")
    course = models.ForeignKey("Course")
    semester = models.SmallIntegerField(verbose_name="學期")
    contract_template = models.ForeignKey("ContractTemplate", blank=True, null=True)
    class_type_choices = (
        (0, "脫產"),
        (1, "周末"),
        (2, "網路班")
    )
    class_type = models.SmallIntegerField(choices=class_type_choices, default=0)
    teachers = models.ManyToManyField("UserProfile", verbose_name="講師")
    start_date = models.DateField(verbose_name="開班日期")
    graduate_date = models.DateField(verbose_name="畢業日期", blank=True, null=True)

    def __str__(self):
        return "%s(%s)期" % (self.course.name, self.semester)

    class Meta:
        unique_together = ("branch", "course", "semester", "class_type")


class CourseRecord(models.Model):
    """課程紀錄表"""
    class_grade = models.ForeignKey("ClassList", verbose_name="上課班級")
    day_num = models.PositiveSmallIntegerField(verbose_name="課程節次")
    teacher = models.ForeignKey("UserProfile")
    title = models.CharField(max_length=64, verbose_name="本節主題")
    content = models.TextField(verbose_name="本節內容")
    has_homework = models.BooleanField(default=True, verbose_name="本節有作業")
    homework = models.TextField(blank=True, null=True, verbose_name="作業需求")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s第%s節" % (self.class_grade, self.day_num)

    class Meta:
        unique_together = ("class_grade", "day_num")


class StudyRecord(models.Model):
    """學習紀錄表(出席、成績等)"""
    course_record = models.ForeignKey("CourseRecord")
    student = models.ForeignKey("Student")
    score_choices = (
        (100, "A+"),
        (90, "A"),
        (85, "B+"),
        (80, "B"),
        (75, "B-"),
        (70, "C+"),
        (60, "C"),
        (40, "C-"),
        (-50, "D"),
        (0, "N/A"),  # not available
        (-100, "COPY"),
    )
    score = models.SmallIntegerField(choices=score_choices, default=0)
    show_choices = (
        (0, "缺席"),
        (1, "出席"),
        (2, "遲到"),
        (3, "早退"),
    )
    show_status = models.SmallIntegerField(default=1, choices=show_choices)
    note = models.TextField(blank=True, null=True, verbose_name="備註")

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s %s" % (self.course_record, self.student, self.score)


class Branch(models.Model):
    """校區表"""
    name = models.CharField(max_length=64, unique=True)
    addr = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name


class Menus(models.Model):
    """動態菜單"""
    name = models.CharField(max_length=64)
    url_type_choices = (
        (0, "absolute"),
        (1, "dynamic"),
    )
    url_type = models.SmallIntegerField(choices=url_type_choices, default=0)
    url_name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "url_name")


"""
還未加入之表:
權限、合同、問卷
"""


class ContractTemplate(models.Model):
    """合同模板"""
    name = models.CharField(max_length=64)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.name


class StudentEnrollment(models.Model):
    """學員報名表"""
    customer = models.ForeignKey("CustomerInfo")
    class_grade = models.ForeignKey("ClassList")
    consultant = models.ForeignKey("UserProfile")
    contract_agreed = models.BooleanField(default=False)
    contract_signed_date = models.DateField(blank=True, null=True)
    contract_approved = models.BooleanField(default=False)
    contract_approved_date = models.DateField(verbose_name="合同審核時間", blank=True, null=True)

    class Meta:
        unique_together = ("customer", "class_grade")

    def __str__(self):
        return "%s" % self.customer


class PaymentRecord(models.Model):
    """繳費紀錄表"""
    enrollment = models.ForeignKey("StudentEnrollment")
    payment_type_choices = (
        (0, "報名費"),
        (1, "學費"),
        (2, "退費"),
    )
    payment_type = models.IntegerField(choices=payment_type_choices, default=0)
    amount = models.IntegerField(verbose_name="費用", default=500)
    consultant = models.ForeignKey("UserProfile")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.enrollment


# from django.contrib.auth.models import User
# class UserProfile(models.Model):
#     """用戶信息表(員工、講師使用)"""
#     user = models.OneToOneField(User)  # 關聯django內建用戶
#     name = models.CharField(max_length=64, verbose_name="姓名")
#     role = models.ManyToManyField("Role", blank=True, null=True)
#
#     def __str__(self):
#         return self.name
