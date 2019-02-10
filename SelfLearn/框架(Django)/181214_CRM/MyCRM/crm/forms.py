from django.forms import ModelForm, forms
from crm import models


class EnrollmentForm(ModelForm):
    def __new__(cls, *args, **kwargs):
        # cls.base_fields 所有字段字典({字段名: 字段對象})
        for field_name in cls.base_fields:
            field_obj = cls.base_fields[field_name]
            field_obj.widget.attrs.update({"class": "form-control"})
            # 唯讀處理
            if field_name in cls.Meta.readonly_fields:
                field_obj.widget.attrs.update({"disabled": "true"})
        return ModelForm.__new__(cls)

    class Meta:
        model = models.StudentEnrollment
        fields = "__all__"
        exclude = ["contract_approved_date"]
        readonly_fields = ["contract_agreed", "contract_signed_date"]

    def clean(self):  # 整體字段額外驗證
        # print("cleaned_data", self.cleaned_data)

        if self.errors:
            raise forms.ValidationError(("Please fix errors before re-submit"))  # 發起表單級別的錯誤
        # 把唯獨資料從舊的資料中取出並覆蓋前端傳回的值，以防別人惡意竄改
        if self.instance.id is not None:
            for field in self.Meta.readonly_fields:
                old_field_val = getattr(self.instance, field)  # 獲取舊值
                form_val = self.cleaned_data.get(field)  # 前端表單回傳值
                # print("兩者", old_field_val, form_val)
                if old_field_val != form_val:
                    # 發起字段級別的錯誤(字段名, 錯誤信息)
                    self.add_error(
                        field,
                        "Readonly Field: Field should be '{value}', not be '{new_value}'".
                            format(**{'value': old_field_val, 'new_value': form_val}))


class CustomerForm(ModelForm):
    def __new__(cls, *args, **kwargs):
        # cls.base_fields 所有字段字典({字段名: 字段對象})
        for field_name in cls.base_fields:
            field_obj = cls.base_fields[field_name]
            field_obj.widget.attrs.update({"class": "form-control"})
            # 唯讀處理
            if field_name in cls.Meta.readonly_fields:
                field_obj.widget.attrs.update({"disabled": "true"})
        return ModelForm.__new__(cls)

    class Meta:
        model = models.CustomerInfo
        fields = "__all__"
        exclude = ["consult_content", "consult_courses", "status"]
        readonly_fields = ["contact_type", "contact", "consultant", "referral_from", "source"]

    def clean(self):  # 整體字段額外驗證
        # print("cleaned_data", self.cleaned_data)

        if self.errors:
            raise forms.ValidationError(("Please fix errors before re-submit"))  # 發起表單級別的錯誤
        # 把唯獨資料從舊的資料中取出並覆蓋前端傳回的值，以防別人惡意竄改
        if self.instance.id is not None:
            for field in self.Meta.readonly_fields:
                old_field_val = getattr(self.instance, field)  # 獲取舊值
                form_val = self.cleaned_data.get(field)  # 前端表單回傳值
                # print("兩者", old_field_val, form_val)
                if old_field_val != form_val:
                    # 發起字段級別的錯誤(字段名, 錯誤信息)
                    self.add_error(
                        field,
                        "Readonly Field: Field should be '{value}', not be '{new_value}'".
                            format(**{'value': old_field_val, 'new_value': form_val}))
