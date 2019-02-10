from django.shortcuts import render, HttpResponse, redirect
from . import models
import re
# import json


class MenuHelper(object):

    def __init__(self, request, nid):
        # 當前請求的request對象
        self.request = request
        self.nid = nid
        # 透過request.path_info獲取當前url
        self.current_url = request.path_info

        # 當前用戶的所有權限
        self.permission2action_dict = None
        # 當前用戶的URL(葉子)
        self.menu_leaf_list = None
        # 當前用戶的菜單(樹枝)
        self.menu_list = None

        self.session_data()

    def session_data(self):
        """
        獲取當前用戶的所有權限、URL、菜單，並加入當前的request.session
        """
        permission_dict = self.request.session.get('permission_info')
        if permission_dict:  # 已存在
            self.permission2action_dict = permission_dict['permission2action_dict']
            self.menu_leaf_list = permission_dict['menu_leaf_list']
            self.menu_list = permission_dict['menu_list']
        else:  # 未存在
            # ----------------------------獲取角色列表----------------------------
            # ----如果是使用內建的多對多 m = models.ManyToManyField("Role")----
            # user_obj = models.User.objects.filter(username=self.nid).first()
            # role_list = user_obj.m.all()

            # ----自建第三張表(方式一)----
            # user_obj = models.User.objects.filter(id=self.nid).first()
            # role_list = models.Role.objects.filter(user2role__u=user_obj)

            # ----自建第三張表(方式二)----
            role_list = models.Role.objects.filter(user2role__u__id=self.nid)
            # ----------------------------獲取角色列表----------------------------

            # --------------------------獲取權限列表&字典-------------------------
            # 方式一
            # permission2action_list = models.Permission2Action2Role.\
            #     objects.filter(r__in=role_list).values("p2a__p__url",
            #                                            "p2a__a__code").distinct()

            # 方式二
            permission2action_list = models.Permission2Action.objects. \
                filter(permission2action2role__r__in=role_list). \
                values('p__url', 'a__code').distinct()

            """
            轉換樣式，方便以後調用
            permission2action_list = [
                {'url':'/index.html','code':'GET'},
                {'url':'/index.html','code':'POST'},
                {'url':'/order.html','code':'GET'},
            ]
            =>
            permission2action_dict = {
                '/index.html':['GET', 'POST']
            }
            """
            permission2action_dict = {}
            for item in permission2action_list:
                if item['p__url'] in permission2action_dict:
                    permission2action_dict[item['p__url']].append(item['a__code'])
                else:
                    permission2action_dict[item['p__url']] = [item['a__code'], ]
            # --------------------------獲取權限列表&字典--------------------------

            # --------------------------獲取菜單葉子列表---------------------------
            # 強制轉型為list，因為session會涉及json轉換，而queryset不支持直接序列化
            # 全部相關且與菜單有關係之url(為菜單中可顯示的權限) --在最後一層
            menu_leaf_list = list(models.Permission2Action.objects.
                                  filter(permission2action2role__r__in=role_list).exclude(p__menu__isnull=True).
                                  values('p_id', 'p__url', 'p__caption', 'p__menu').distinct())
            # --------------------------獲取菜單葉子列表---------------------------

            # ----------------------------獲取菜單列表-----------------------------
            # 強制轉型為list，因為session會涉及json轉換，而queryset不支持直接序列化
            menu_list = list(models.Menu.objects.values('id', 'caption', 'parent_id'))
            # ----------------------------獲取菜單列表-----------------------------

            # 加入session
            self.request.session['permission_info'] = {
                'permission2action_dict': permission2action_dict,
                'menu_leaf_list': menu_leaf_list,
                'menu_list': menu_list,
            }

            # 設置參數
            self.permission2action_dict = permission2action_dict
            self.menu_leaf_list = menu_leaf_list
            self.menu_list = menu_list

    def menu_data_list(self):
        menu_leaf_dict = {}  # 葉子
        open_leaf_parent_id = None

        # --------------------------獲取菜單葉子列表---------------------------
        for item in self.menu_leaf_list:
            # {"p_id":1. 'p__caption': 2, 'p__url': '/userinfo.html', 'p__menu': '用戶管理'}
            item = {  # 轉換key，為了跟菜單字典配合
                'id': item['p_id'],
                'url': item['p__url'],
                'caption': item['p__caption'],
                'parent_id': item['p__menu'],
                'child': [],
                'status': True,  # 為了方便後面判斷是否要顯示該菜單
                'open': False  # 為了方便後面判斷是否要打開該菜單
            }
            if item['parent_id'] in menu_leaf_dict:
                menu_leaf_dict[item['parent_id']].append(item)
            else:
                menu_leaf_dict[item['parent_id']] = [item, ]
            # 判斷url葉子是否打開，因為上面加入字典的為內存地址，所以我們這邊改動，字典內的也會連動改變
            if re.match(item['url'], self.current_url):
                item['open'] = True
                open_leaf_parent_id = item['parent_id']
        # --------------------------獲取菜單葉子列表---------------------------

        # ----------------------------獲取菜單字典-----------------------------
        menu_dict = {}  # 樹枝
        for item in self.menu_list:
            item['child'] = []
            item['status'] = False
            item['open'] = False
            menu_dict[item['id']] = item
        # ----------------------------獲取菜單字典-----------------------------

        # ---------------------------結合樹枝和葉子----------------------------
        for k, v in menu_leaf_dict.items():
            menu_dict[k]['child'] = v
            parent_id = k
            # 將父代中有葉子節點的菜單設為【顯示】
            while parent_id:
                menu_dict[parent_id]['status'] = True
                parent_id = menu_dict[parent_id]['parent_id']
        # ---------------------------結合樹枝和葉子----------------------------

        # ------------------------菜單樹枝是否設為打開-------------------------
        # 將父代中有葉子節點的菜單設為【展開】
        while open_leaf_parent_id:
            menu_dict[open_leaf_parent_id]['open'] = True
            open_leaf_parent_id = menu_dict[open_leaf_parent_id]['parent_id']
        # ------------------------菜單樹枝是否設為打開-------------------------

        # --------------------------樹枝間的等級關係---------------------------
        result = []  # 樹狀架構
        for row in menu_dict.values():
            if not row['parent_id']:
                result.append(row)
            else:
                menu_dict[row['parent_id']]['child'].append(row)
        # --------------------------樹枝間的等級關係---------------------------
        return result

    def menu_tree(self, result):
        response = ""
        tpl = """
        <div class="item %s">
            <div class="title">%s</div>
            <div class="content">%s</div>
        </div>
        """
        for row in result:
            if not row['status']:  # 不需顯示的菜單則跳過(status=False)
                continue

            active = ""
            if row['open']:  # 當前打開的菜單設置active
                active = "active"

            if 'url' in row:  # 有url表示此row是葉子(最後一層)
                response += "<a class='%s' href='%s'>%s</a>" % (active, row['url'], row['caption'])
            else:  # 不是葉子就繼續往下搜，直到樹枝末尾或葉子為止
                title = row['caption']
                content = self.menu_tree(row['child'])
                response += tpl % (active, title, content)
        return response

    def actions(self):
        """
        檢查當前用戶是否有此URL之權限，並獲取此URL之權限操作
        """
        action_list = []
        # {
        #     '/index.html': ['GET',POST,]
        # }
        for k, v in self.permission2action_dict.items():
            print(k, v)
            if re.match(k, self.current_url):
                action_list = v  # ['GET',POST,]
                break
        return action_list


def permission(func):
    """
    驗證權限裝飾器
    """
    def inner(request, *args, **kwargs):
        user_info = request.session.get('user_info')
        if not user_info:
            return redirect('/login.html')
        obj = MenuHelper(request, user_info['nid'])
        action_list = obj.actions()
        if not action_list:
            return HttpResponse('無權限訪問')
        kwargs['menu_string'] = obj.menu_tree(obj.menu_data_list())
        kwargs['action_list'] = action_list
        return func(request, *args, **kwargs)
    return inner


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        obj = models.User.objects.filter(username=username, password=pwd).first()
        if obj:
            # 當前用戶信息放置於session中
            request.session['user_info'] = {'nid': obj.id, 'username': obj.username}

            MenuHelper(request, obj.id)
            return redirect('/index.html')
        else:
            return redirect('/login.html')


def logout(request):
    request.session.clear()
    return redirect('/login.html')


@permission
def index(request, *args, **kwargs):
    # print("args", args)
    # print("kwargs", kwargs)
    action_list = kwargs.get('action_list')
    menu_string = kwargs.get('menu_string')
    # 有查看之功能則呈現數據
    if "get" in action_list:
        result = models.User.objects.all()
    else:
        result = []
    return render(request, 'index.html', {'menu_string': menu_string, 'action_list': action_list})


@permission
def report(request, *args, **kwargs):
    action_list = kwargs.get('action_list')
    menu_string = kwargs.get('menu_string')

    if "get" in action_list:
        result = models.User.objects.all()
    else:
        result = []
    return render(request, 'report.html', {'menu_string': menu_string, 'action_list': action_list})


@permission
def article(request, *args, **kwargs):
    action_list = kwargs.get('action_list')
    menu_string = kwargs.get('menu_string')

    if "get" in action_list:
        result = models.User.objects.all()
    else:
        result = []
    return render(request, 'article.html', {'menu_string': menu_string, 'action_list': action_list})

# class MenuHelper(object):
#     def __init__(self, username, user_request_url):
#         self.username = username
#         self.current_url = user_request_url
#         self.result = None
#         self.p2a_list = None
#         self.init_data()
#
#     def init_data(self):
#         # ---------------------------------角色列表---------------------------------
#         # ----如果是使用內建的多對多 m = models.ManyToManyField("Role")---- role_list
#         # user_obj = models.User.objects.filter(username=username).first()
#         # role_list = user_obj.m.all()
#
#         # ----自建第三張表(方式一)---- user2role_list
#         # user_obj = models.User.objects.filter(username=username).first()
#         # user2role_list = models.User2Role.objects.filter(u=user_obj)
#         # print(user2role_list)
#
#         # ----自建第三張表(方式二)---- role_list
#         # user_obj = models.User.objects.filter(username=username).first()
#         # role_list = models.Role.objects.filter(user2role__u=user_obj)
#         # print(role_list)
#
#         # ----自建第三張表(方式三)---- role_list
#         role_list = models.Role.objects.filter(user2role__u__username=self.username)
#         print(role_list)
#
#         # ---------------------------------權限列表---------------------------------
#         # 方式一:
#         # p2a_list = models.Permission2Action.objects.filter(permission2action2role__r__in=role_list).values("p__url",
#         #                                                                                                    "a__code")
#         # print(p2a_list)
#
#         # 方式二
#         p2a_list = models.Permission2Action2Role.objects. \
#             filter(r__in=role_list).values("p2a__p__url",
#                                            "p2a__p__id",
#                                            "p2a__a__code",
#                                            "p2a__a__id").distinct()
#
#         # 最後將獲取的權限列表放到session中，缺點：無法即時更新，須讓用戶重新登入 (沒寫)
#         self.p2a_list = p2a_list
#         # for row in p2a_list:
#         #     print(row)
#
#         # 全部相關之url
#         # url_list = models.Permission2Action2Role.objects. \
#         #     filter(r__in=role_list).values("p2a__p__url", "p2a__p__caption").distinct()
#         # for row in url_list:
#         #     print(row)
#
#         # 全部相關且與菜單有關係之url(為菜單中可顯示的權限) --在最後一層
#         menu_leaf_list = models.Permission2Action2Role.objects. \
#             filter(r__in=role_list).exclude(p2a__p__menu__isnull=True). \
#             values("p2a__p_id", "p2a__p__url", "p2a__p__caption", "p2a__p__menu").distinct()
#
#         open_leaf_parent_id = None
#         menu_leaf_dict = {}  # 葉子
#         for row in menu_leaf_list:
#             # {"p2a__p_id":1. 'p2a__p__menu': 2, 'p2a__p__url': '/userinfo.html', 'p2a__p__caption': '用戶管理'}
#             item = {  # 轉換key，為了跟菜單字典配合
#                 "id": row["p2a__p_id"],
#                 "url": row["p2a__p__url"],
#                 "caption": row["p2a__p__caption"],
#                 "parent_id": row["p2a__p__menu"],
#                 "child": [],
#                 "status": True,  # 為了方便後面判斷是否要顯示該菜單
#                 "open": False,  # 為了方便後面判斷是否要打開該菜單
#             }
#
#             # 判斷url葉子是否打開
#             if re.match(item["url"], self.current_url):
#                 item["open"] = True
#                 open_leaf_parent_id = item["parent_id"]
#
#             if item["parent_id"] in menu_leaf_dict:  # 存在則添加
#                 menu_leaf_dict[item["parent_id"]].append(item)
#             else:  # 不存在則創建
#                 menu_leaf_dict[item["parent_id"]] = [item, ]
#
#         # ---------------------------------菜單列表&字典---------------------------------
#         menu_list = models.Menu.objects.values("id", "caption", "parent_id")
#         menu_dict = {}  # 樹枝
#         for row in menu_list:
#             row["child"] = []  # 初始值為 []
#             row["status"] = False  # 初始值為 False
#             row["open"] = False  # 初始值為 False
#             menu_dict[row["id"]] = row
#         # for k, v in menu_dict.items():
#         #     print(k, v)
#
#         # ---------------------------------菜單樹枝是否設為打開---------------------------------
#         while open_leaf_parent_id:
#             menu_dict[open_leaf_parent_id]["open"] = True
#             open_leaf_parent_id = menu_dict[open_leaf_parent_id]["parent_id"]
#
#         # ---------------------------結合樹枝和葉子---------------------------
#         for k, v in menu_leaf_dict.items():
#             menu_dict[k]["child"] = v  # 將葉子加入對應樹枝的child
#             parent_id = k
#             while parent_id:  # 並將相關樹枝們的status設成True
#                 menu_dict[parent_id]["status"] = True
#                 parent_id = menu_dict[parent_id]["parent_id"]
#         # print(json.dumps(menu_dict, ensure_ascii=False))
#         # for k, v in menu_dict.items():
#         #     print(k, v)
#
#         # -------------------------------樹枝間的等級關係-------------------------------
#         result = []
#         for row in menu_dict.values():
#             if row["parent_id"]:
#                 menu_dict[row["parent_id"]]["child"].append(row)
#             else:
#                 result.append(row)  # result中只放根菜單(也就是parent_id=None的菜單)
#
#         # for k, v in menu_dict.items():
#         #     print(k, v)
#         # for row in result:
#         #     print(row)
#         self.result = result
#
#     def menu_tree(self, result):
#         response = ""
#         tpl = """
#         <div class="item %s">
#             <div class="title">%s</div>
#             <div class="content">%s</div>
#         </div>
#         """
#         for row in result:
#             if not row["status"]:  # 不需顯示的菜單則跳過(status=False)
#                 continue
#
#             active = ""
#             if row["open"]:  # 當前打開的菜單設置active
#                 active = "active"
#
#             if "url" in row:  # 有url表示此row是葉子(最後一層)
#                 response += "<a class='%s' href='%s'>%s</a>" % (active, row["url"], row["caption"])
#             else:  # 不是葉子就繼續往下搜，直到樹枝末尾或葉子為止
#                 title = row["caption"]
#                 content = self.menu_tree(row["child"])
#                 response += tpl % (active, title, content)
#
#         return response


# def index(request):
#     username = request.session["user_info"]["username"]  # 先假設用戶已登入
#     user_request_url = "/report.html"  # 先假設這為用戶訪問之網址
#
#     menuhelper = MenuHelper(username, user_request_url)
#     result = menuhelper.result
#     # 最後將獲取的權限列表放到session中，缺點：無法即時更新，須讓用戶重新登入 (沒寫)
#     p2a_list = menuhelper.p2a_list
#
#     # ----------------------------------生成菜單----------------------------------
#     # 不能使用for循環，因為我們不知道菜單總共會有幾層
#     # for row in result:
#     #     print(row["caption"])
#     #     for row2 in row["child"]:
#     #         print("----", row2["caption"])
#     #         for row3 in row2["child"]:
#     #             print("--------", row3["caption"])
#
#     # 所以要用函數遞歸實現
#     menu_string = menuhelper.menu_tree(result)
#
#     return render(request, "index.html", {"menu_string": menu_string})
