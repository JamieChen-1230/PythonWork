from django import conf


def kingadmin_auto_discover():
    # conf會自動抓取當前項目，如果是用from MyCRM import settings，就會被寫死了
    for app_name in conf.settings.INSTALLED_APPS:
        try:
            mod = __import__("%s.kingadmin" % app_name)
            print(mod.kingadmin)
        except ImportError:
            pass
