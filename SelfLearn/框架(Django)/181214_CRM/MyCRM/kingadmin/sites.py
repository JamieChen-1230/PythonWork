from kingadmin.admin_base import BaseKingAdmin


class AdminSite(object):
    """
    自定義Admin,
    仿效Django的Admin製作
    """
    def __init__(self):
        """
            格式:
            enabled_admins = {
                    "App名": {"小寫表名": admin_class,  }
                    "crm":  {"customer":  CustomerAdmin, }
            }
            """
        self.enabled_admins = {}

    def register(self, model_class, admin_class=BaseKingAdmin):
        """註冊admin表"""
        print("register", model_class, admin_class)
        # 透過表獲取App名稱
        app_name = model_class._meta.app_label
        # 透過表獲取表名(小寫)
        model_name = model_class._meta.model_name

        # 把model_class賦值給admin_class, 讓以後能透過admin_class取到model_class
        # admin_class.model = model_class
        # 但因為都用同一個class的內存會相互覆蓋掉值, 所以需先實例化變成獨立個體後再賦值
        admin_obj = admin_class()
        admin_obj.model = model_class

        if app_name not in self.enabled_admins:
            self.enabled_admins[app_name] = {}
        self.enabled_admins[app_name][model_name] = admin_obj


# python幫我們做過優化，所以我們在多處import site 時，不會重複實例化，讓我們的enabled_admins能達到共用效果
site = AdminSite()  # 實例化對象, 方便之後調用方法
