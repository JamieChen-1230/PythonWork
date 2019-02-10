from django.forms import ModelForm
from crm import models


# 一般創建class方法
# class CustomerForm(ModelForm):
#     class Meta:
#         model = models.CustomerInfo
#         fields = "__all__"
#
#     # Django修改字段的程序在__new__方法中
#     def __new__(cls, *args, **kwargs):
#         print("new", cls, args, kwargs)
#         # cls.base_fields 所有字段字典({字段名: 字段對象})
#         for field_name in cls.base_fields:
#             field_obj = cls.base_fields[field_name]
#             field_obj.widget.attrs.update({"class": "form-control"})
#         return super().__new__(cls)


def create_dynamic_model_form(admin_class, form_add=False):
    """
    動態生成model_form
    form_add=False: 表示為修改之表單
    form_add=True: 表示為添加之表單
    """

    class Meta:
        model = admin_class.model  # 讓ModelForm與model之間建立關聯
        fields = "__all__"  # 所有字段
        # fields = ['status']  # 顯示指定字段
        # exclude = ['name']  # 排除指定字段

    # Django修改字段的程序在__new__方法中
    def __new__(cls, *args, **kwargs):
        # cls.base_fields 所有字段字典({字段名: 字段對象})
        for field_name in cls.base_fields:
            field_obj = cls.base_fields[field_name]
            field_obj.widget.attrs.update({"class": "form-control"})
            # 唯讀處理
            if (field_name in admin_class.readonly_fields) and (not form_add):
                field_obj.widget.attrs.update({"readonly": "true",
                                               "onfocus": "defaultValue=this.value",
                                               "onchange": "this.value=defaultValue"})
        return ModelForm.__new__(cls)

    # 動態創建class -- type(類名, (要繼承的類,), {方法名: 方法, })
    dynamic_form = type("DynamicModelForm", (ModelForm,), {"Meta": Meta, "__new__": __new__})
    # print(dynamic_form)
    return dynamic_form
