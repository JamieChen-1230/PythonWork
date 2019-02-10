from django.core.urlresolvers import resolve
from django.shortcuts import render, redirect
from kingadmin.permission_list import perm_dic
from django.conf import settings


def perm_check(*args, **kwargs):
    """
    1. 獲取當前請求的url
    2. 把url反解成url_name(別名)
    3. 判斷用戶是否已登錄
    4. 拿url_name到perm_dict去匹配，匹配包括url_name, 方法, 參數
    5. 拿到權限key(perm_dict的key)，調用user.has_perm(key)
    """
    request = args[0]
    """request.path獲取當前請求的url"""
    resolve_url_obj = resolve(request.path)  # resolve("網址") 為ResolverMatch對象
    """反解出url_name(當前url別名)"""
    current_url_name = resolve_url_obj.url_name
    # print('---perm:', request.user, request.user.is_authenticated(), current_url_name)
    match_key = None
    match_results = [None]
    """判斷用戶是否已登錄"""
    if request.user.is_authenticated() is False:  # 要登入成功才可繼續驗證
        return redirect(settings.LOGIN_URL)

    for permission_key, permission_val in perm_dic.items():
        # 取出對應的key和所有value
        per_url_name = permission_val[0]
        per_method = permission_val[1]
        perm_args = permission_val[2]
        perm_kwargs = permission_val[3]
        perm_hook_func = permission_val[4] if len(permission_val) > 4 else None  # 因為不一定有鉤子函數，所以要判斷

        """url_name匹配"""
        if per_url_name == current_url_name:  # matches current request url
            """請求方法(GET/POST)匹配"""
            if per_method == request.method:  # matches request method
                args_matched = False
                """[] 不特定參數匹配"""
                for item in perm_args:  # 逐一對應，看哪個能匹配上
                    request_method_func = getattr(request, per_method)  # request.GET/POST
                    if request_method_func.get(item, None):  # request.method中有此參數
                        args_matched = True
                    else:
                        args_matched = False
                        break  # 只要有一個參數匹配不到就直接退出迴圈
                else:  # for-else語法，只要沒有被break,return等中斷迴圈，循環結束後都會執行
                    args_matched = True  # 當perm_args=[]或都匹配上了時執行

                """{} 特定參數匹配"""
                kwargs_matched = False
                for k, v in perm_kwargs.items():
                    request_method_func = getattr(request, per_method)
                    arg_val = request_method_func.get(k, None)  # request.method中有此參數
                    # print("perm kwargs check:", arg_val, type(arg_val), v, type(v))
                    if arg_val == str(v):  # 不只要有那個參數，值也必須匹配上
                        kwargs_matched = True
                    else:
                        kwargs_matched = False
                        break  # 只要有一個參數匹配不到就直接退出迴圈
                else:
                    kwargs_matched = True

                """func 自定義匹配權限鉤子函數(返回True或False)"""
                perm_hook_matched = True
                if perm_hook_func:
                    perm_hook_matched = perm_hook_func(request)

                match_results = [args_matched, kwargs_matched, perm_hook_matched]
                # print("--->match_results ", match_results)
                # all()列表裡的元素都為真才為True
                if all(match_results):  # 所有參數都匹配上了
                    match_key = permission_key
                    break

    if all(match_results):
        # 第一個值賦給app_name，剩下的給per_name
        app_name, *per_name = match_key.split('_')
        # print("--->matched ", match_results, match_key)
        print(app_name, *per_name)
        perm_obj = '%s.%s' % (app_name, match_key)  # EX: crm.crm_table_index
        # print("perm str:", perm_obj)
        """調用user.has_perm(key)"""
        if request.user.has_perm(perm_obj):  # 判斷是否有此權限，參數為 app_name.權限名
            # print("--->request.user", request.user)
            # print("--->request.user", type(request.user))
            print('有權限')
            return True
        else:
            print('無權限')
            return False
    else:
        print("無此權限")


def check_permission(func):
    """驗證權限裝飾器"""
    def inner(*args, **kwargs):
        if not perm_check(*args, **kwargs):
            # 如果無權限則返回403頁面
            request = args[0]
            return render(request, 'kingadmin/page_403.html')
        # 如果驗證成功，執行原方法內容
        return func(*args, **kwargs)
    return inner
