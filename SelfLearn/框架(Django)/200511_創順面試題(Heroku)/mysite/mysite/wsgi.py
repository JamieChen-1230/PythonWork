"""
heroku處理靜態檔案的方式與本機不相同
而且為了讓heroku能夠透過wsgi與我們的網站溝通
"""
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling  # <- 加入

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
application = Cling(get_wsgi_application())  # <- 修改
