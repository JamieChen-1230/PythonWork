"""
通常正式上線（production）時的環境會和開發時所做的settings.py設定有所不同
而且我們希望網站上線時使用一個全新的、空白的資料庫
以便與原本測試用的資料庫來做區分
所以我們另外建立一個production_settings.py，放在原本的settings.py旁邊
"""

import dj_database_url
from .settings import *  # 含入原本的settings.py所有設定
# heroku使用的資料庫為PostgreSQL，所以要修改資料庫設定
DATABASES = {
    'default': dj_database_url.config(),
}


# 設定專案讓它能在Heroku上正確提供靜態檔
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # 設定網站正式上線時靜態檔案目錄位置
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'nba', 'static'),
)


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # 設定HTTP連線方式
ALLOWED_HOSTS = ['*']  # 讓所有的網域都能瀏覽本網站
DEBUG = False  # 關閉除錯模式
