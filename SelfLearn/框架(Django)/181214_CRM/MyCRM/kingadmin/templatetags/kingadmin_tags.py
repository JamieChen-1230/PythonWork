from django.template import Library
from django.utils.safestring import mark_safe
import datetime

register = Library()


@register.simple_tag
def build_table_row(obj, admin_class):
    """生成一條紀錄的html element"""
    ele = ""
    if admin_class.list_display:
        # enumerate()用於可遍歷的對象(如列表、元組或字符串)，可同時抓到數據和數據下標，一般用在for循環當中
        for index, column_name in enumerate(admin_class.list_display):
            # models.xxx表._meta.fields 獲取xxx表的所有字段對象
            # models.xxx表._meta.get_field("status") 獲取xxx表的status字段對象
            column_obj = admin_class.model._meta.get_field(column_name)
            # 判斷字段是否有choices屬性
            if column_obj.choices:
                # 有, 要找出對應之值
                # get_xx字段_display
                column_data = getattr(obj, "get_%s_display" % column_name)()
            else:
                # 無, 直接找
                column_data = getattr(obj, column_name)

            td_ele = "<td>%s</td>" % column_data
            if index == 0:  # 第一欄作為進入增刪改查進入點
                td_ele = "<td><a href='%s/change/'>%s</a></td>" % (obj.id, column_data)
            ele += td_ele
    else:
        td_ele = "<td><a href='%s/change/'>%s</a></td>" % (obj.id, obj)
        ele += td_ele

    return mark_safe(ele)


@register.simple_tag
def build_filter_ele(filter_column, admin_class):
    """list_filter過濾條件"""
    filter_ele = "<select class='form-control' name='%s'>" % filter_column
    column_obj = admin_class.model._meta.get_field(filter_column)
    # .get_choices()就算沒有choices屬性, 他也會根據資料組成((id, 值),)列表, 但DateField不適用
    try:
        for choice in column_obj.get_choices():
            option_ele = "<option value='%s'>%s</option>" % (choice[0], choice[1])
            if filter_column in admin_class.filter_conditions:  # 當前字段已被過濾
                if str(choice[0]) == admin_class.filter_conditions.get(filter_column):  # 且當前值被選中
                    option_ele = "<option value='%s' selected='selected'>%s</option>" % (choice[0], choice[1])  # 被選中
            filter_ele += option_ele
    except AttributeError as e:
        print("err", e)
        # .get_internal_type() 獲取Field類型
        if column_obj.get_internal_type() in ('DateField', 'DateTimeField'):
            filter_ele = "<select class='form-control' name='%s__gte'>" % filter_column
            today = datetime.datetime.now()
            time_list = [
                ["", "---------"],
                [today, "Today"],
                [today-datetime.timedelta(7), "七天內"],
                [today.replace(day=1), "本月"],
                [today-datetime.timedelta(90), "三個月內"],
                [today.replace(month=1, day=1), "本年"],
            ]

            for t in time_list:
                # if t[0]:
                #     option_ele = "<option value='%s'>%s</option>" % (t[0].strftime("%Y-%m-%d"), t[1])
                # else:
                #     option_ele = "<option value='%s'>%s</option>" % (t[0], t[1])
                # 三元表達式
                time_to_str = '' if not t[0] else t[0].strftime("%Y-%m-%d")
                option_ele = "<option value='%s'>%s</option>" % (time_to_str, t[1])
                if ("%s__gte" % filter_column) in admin_class.filter_conditions:  # 當前字段已被過濾
                    if time_to_str == admin_class.filter_conditions.get("%s__gte" % filter_column):  # 且當前值被選中
                        option_ele = "<option value='%s' selected='selected'>%s</option>" % (time_to_str, t[1])
                filter_ele += option_ele

    filter_ele += "</select>"
    return mark_safe(filter_ele)


@register.simple_tag
def get_model_name(admin_class):
    return admin_class.model._meta.model_name.upper()


@register.simple_tag
def render_paginator_btn(querysets, admin_class):
    ele = """<ul class="pagination" style='margin: 0px;'>"""
    print(admin_class.filter_conditions)

    # 要保留過濾條件
    condition_str = ""
    # 條件過濾
    for key, val in admin_class.filter_conditions.items():
        condition_str += "%s=%s&" % (key, val)
    # 排序過濾
    for key, val in admin_class.orderby_conditions.items():
        condition_str += "%s=%s&" % ("_o", val)
    # 搜尋過濾
    condition_str += "%s=%s&" % ("_q", admin_class.search_key)

    if querysets.has_previous():  # 有上一頁
        ele += '''<li><a href="?%s_page=%s">上一頁</a></li>''' % (condition_str, querysets.previous_page_number())
    else:
        ele += '''<li class='disabled'><a href="#">上一頁</a></li>'''

    # querysets.paginator等同於paginator
    for i in querysets.paginator.page_range:
        if abs(querysets.number - i) < 3:  # 要顯示之頁碼數量
            li_ele = '''<li><a href="?%s_page=%s">%s</a></li>''' % (condition_str, i, i)
            if querysets.number == i:  # 當前頁
                li_ele = '''<li class="active"><a href="?%s_page=%s">%s</a></li>''' % (condition_str, i, i)
            ele += li_ele

    if querysets.has_next():  # 有下一頁
        ele += '''<li><a href="?%s_page=%s">下一頁</a></li>''' % (condition_str, querysets.next_page_number())
    else:
        ele += '''<li class='disabled'><a href="#">下一頁</a></li>'''
    ele += "</ul>"

    return mark_safe(ele)


@register.simple_tag
def get_orderby_index(admin_class, column, forloop):
    if column in admin_class.orderby_conditions:  # 是否有被排序
        if not admin_class.orderby_conditions[column].startswith("-"):  # 目前為正序
            return "-" + admin_class.orderby_conditions[column]
    return forloop["counter0"]


@register.simple_tag
def render_orderby_icon(admin_class, column):
    if column in admin_class.orderby_conditions:  # 是否有被排序
        if not admin_class.orderby_conditions[column].startswith("-"):  # 目前為正序
            ele = """<span class="glyphicon glyphicon-triangle-top" aria-hidden="true"></span>"""
        else:  # 目前為倒序
            ele = """<span class="glyphicon glyphicon-triangle-bottom" aria-hidden="true"></span>"""
        return mark_safe(ele)
    return ""


@register.simple_tag
def render_filtered_args(admin_class):
    condition_str = ""
    # 條件過濾
    if admin_class.filter_conditions:
        for key, val in admin_class.filter_conditions.items():
            condition_str += "&%s=%s" % (key, val)
        return condition_str
    # 搜尋過濾
    if admin_class.search_key:
        condition_str += "&%s=%s" % ("_q", admin_class.search_key)
    return condition_str


@register.simple_tag
def render_ordered_args(admin_class):
    values = ""
    for key, val in admin_class.orderby_conditions.items():
        values = val
    return values


@register.simple_tag
def get_readonly_field_val(form_obj, field_name):
    """返回唯獨字段內容"""
    return getattr(form_obj.instance, field_name)


@register.simple_tag
def get_available_m2m_data(field_name, form_obj, admin_class, form_add):
    """返回m2m字段關聯表的所有未選數據"""
    field_obj = admin_class.model._meta.get_field(field_name)
    obj_list = field_obj.related_model.objects.all()  # 所有數據
    all_set = set(obj_list)
    if form_add:
        # Add
        return all_set
    else:
        # Change
        selected_data = getattr(form_obj.instance, field_name).all()  # 已選數據
        selected_set = set(selected_data)
        return all_set - selected_set  # 未選數據


@register.simple_tag
def get_selected_m2m_data(field_name, form_obj, admin_class, form_add):
    """返回m2m字段已選的所有數據"""
    if form_add:
        # Add
        return {}
    else:
        # Change
        selected_data = getattr(form_obj.instance, field_name).all()
        return selected_data


@register.simple_tag
def display_all_related_obj(obj):
    """列出欲刪除對象的所有關聯對象 """
    ele = "<ul><a href='/kingadmin/%s/%s/%s/change/'>%s</a>" % (
        obj._meta.app_label, obj._meta.model_name, obj.id, obj)
    ele += recursion_releted_obj(obj)
    ele += "</ul>"
    return ele


def recursion_releted_obj(obj):
    """
    obj._meta.fields   裡面包含FK
    obj._meta.related_objects  反向關聯'、自關聯
    obj._meta.many_to_many  多對多關聯
    field.get_internal_type()  字段類型
    field.name  字段名
    model.name  表名
    """
    # ForeignKey不需要處理，因為不會刪除到關聯對象
    # 反向關聯(Fk, 1to1, m2m)
    ele = ""
    for reversed_fk_obj in obj._meta.related_objects:
        related_table_name = reversed_fk_obj.name
        if reversed_fk_obj.get_internal_type() == "OneToOneField":
            # 一對一反向查找直接使用表名(小寫)
            related_lookup_key = related_table_name
            # 一對一反向查找出來的只有一個，所以沒有.all()方法，且因為後面要循環，所以把值放入一個陣列
            if getattr(obj, related_lookup_key, ""):
                related_objs = [getattr(obj, related_lookup_key, "")]
            else:
                related_objs = []
        else:
            # FK反向查找使用表名(小寫)_set
            related_lookup_key = "%s_set" % related_table_name
            related_objs = getattr(obj, related_lookup_key).all()  # 反向關聯的對象

        ele += "<li>%s<ul>" % related_table_name
        # print(related_objs)
        if reversed_fk_obj.get_internal_type() == "ManyToManyField":
            # 多對多關聯對象只會受些微影響，不會被刪除
            # 所以不必再進行遞歸深入查找
            for i in related_objs:
                ele += "<li><a href='/kingadmin/%s/%s/%s/change/'>%s</a></li>" % (
                    i._meta.app_label, i._meta.model_name, i.id, i)
        else:
            # 反向FK是會被刪除的，所以須遞歸深入查找
            for i in related_objs:
                ele += "<li><a href='/kingadmin/%s/%s/%s/change/'>%s</a></li>" % (
                    i._meta.app_label, i._meta.model_name, i.id, i)
                ele += recursion_releted_obj(i)  # 遞歸
        ele += "</ul></li>"
    return ele

@register.simple_tag
def get_admin_class(site, app_name, model_name):
    return site.enabled_admins[app_name][model_name]


@register.simple_tag
def get_model_verbose_name(admin_class):
    return admin_class.model._meta.verbose_name
