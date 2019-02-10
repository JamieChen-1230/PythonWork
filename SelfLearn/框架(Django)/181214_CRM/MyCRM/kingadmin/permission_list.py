from kingadmin import permission_hook

perm_dic = {
    "crm_model_list": ["model_list", "GET", [], {}],  # 允許訪問model列表
    'crm_view_my_own_customers': ['model_obj_list', 'GET', [], {}, permission_hook.view_my_own_customers],  # 訪問自定義數據資料頁
    # 'crm_table_list': ['model_obj_list', 'GET', [], {"source": 0, "consultant": 6}],  # 訪問限制數據資料頁
    'crm_table_list': ['model_obj_list', 'GET', [], {}],    # 訪問所有數據資料頁
    'crm_table_list_view': ['model_obj_change', 'GET', [], {}],  # 訪問數據修改頁
    'crm_table_list_change': ['model_obj_change', 'POST', [], {}],    # 可以提交修改
    'crm_model_obj_add_view': ['model_obj_add', 'GET', [], {}],  # 訪問數據增加頁
    'crm_model_obj_add': ['model_obj_add', 'POST', [], {}],  # 可以提交增加
}