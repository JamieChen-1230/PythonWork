from django.conf.urls import url
from app01 import views


urlpatterns = [
    # 以前實現api接口必須創建四個url和view
    url(r'^get_order', view=views.get_order),
    url(r'^add_order', view=views.add_order),
    url(r'^del_order', view=views.del_order),
    url(r'^update_order', view=views.update_order),

    # 現在根據restful規範整合在一個url和view
    # url(r'^order', view=views.order),
    # 更好的是用CBV來實現
    # url(r'^order', view=views.OrderView.as_view()),
    # ※ restful規範(二)：url規範。(讓別人知道這是個api接口)
    #   EX：https://域名/api/版本號/名詞  => https://www.example.com/api/v1/animals
    url(r'^api/v1/orders', view=views.OrderView.as_view()),
]
