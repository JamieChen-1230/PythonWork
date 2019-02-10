# 器本質上就是函數
# 裝飾器：功能是為其他函數添加附加功能
# 原則：1.不修改被修飾函數的原代碼 2.不修改被修飾函數的調用方法
# 裝飾器的知識儲備：裝飾器=高階函數+函數嵌套+閉包

# ------高階函數------
# 高階函數定義：傳入參數是函數名或回傳值是函數名
# 只符合條件一
# import time
# def foo():
#     time.sleep(1)
#     print("你好")
# def test(func):  # 符合不修改被修飾函數的原代碼
#     print(func)  # => <function foo at 0x00000258E0D67F28>
#     start = time.time()
#     func()  # 調用foo()
#     end = time.time()
#     print("運行時間%s" % (end-start))  # => 運行時間1.0005557537078857
# test(foo)  # foo的原調用方法是foo()，但現在卻是test(foo)，所以不是裝飾器

# 符合條件一、二，但會多運行一次被調用函數 (這是高階函數的極限了)
# import time
# def foo():
#     time.sleep(1)
#     print("來自foo")
# # 不修改foo的原代碼
# # 不修改foo的調用方法
# def timmer(func):  # 符合不修改被修飾函數的原代碼
#     start = time.time()
#     func()  # 調用foo()
#     end = time.time()
#     print("運行時間%s" % (end-start))  # => 運行時間1.0005557537078857
#     return func
# foo = timmer(foo)
# foo()  # 符合不修改被修飾函數的調用方法
# # 運行結果如下，但多運行了一次foo()
# # 來自foo
# # 運行時間1.0005180835723877
# # 來自foo

# ------函數嵌套------
# 函數嵌套定義：函數裡面定義函數
# def father(name):
#     print("from father %s" % name)  # => from father jamie
#     def son():  # 函數即變量
#         print(name)  # => jamie
#         def grandson():
#             name = "sb"
#             print(name)  # => sb
#         grandson()
#     print(locals())  # => {'name': 'jamie', 'son': <function father.<locals>.son at 0x0000022C899E5510>}，顯示局部變量
#     son()
# father("jamie")

# ------閉包------
# 閉包定義：封裝變量
# def father(name): # father()封裝了name, son()
#     print("from father %s" % name)  # => from father jamie
#     def son():  # son()封裝了grandson()，因函數即變量
#         print(name)  # => jamie
#         def grandson():  # grandson()封裝了name
#             name = "sb"
#             print(name)  # => sb
#         grandson()
#     print(locals())  # => {'name': 'jamie', 'son': <function father.<locals>.son at 0x0000022C899E5510>}，顯示局部變量
#     son()
# father("jamie")

# ------裝飾器的基本架構(1)------
# import time
# def timmer(func):  # func = test
#     def wrapper():
#         # print(func)
#         start = time.time()
#         func()  # 運行test()
#         end = time.time()
#         print("運行時間%s" % (end - start))
#     return wrapper
#
# @timmer   # @timmer 相當於 test = timmer(test)
# def test():  # 符合不修改被修飾函數的原代碼
#     time.sleep(1)
#     print("test")
#
# # test = timmer(test)  # 得到wrapper的地址
# test()  # 執行wrapper()，符合不修改被修飾函數的調用方法

# ------裝飾器的基本架構+返回值(2)------
# import time
# def timmer(func):  # func = test
#     def wrapper():
#         # print(func)
#         start = time.time()
#         res = func()  # 運行test()
#         end = time.time()
#         print("運行時間%s" % (end - start))
#         return res  # 因為實際上是執行wrapper()，所以要有返回值要從這return
#     return wrapper
#
# @timmer   # @timmer 相當於 test = timmer(test)
# def test():
#     time.sleep(1)
#     print("test")
#     return "test的返回值"
# # test = timmer(test)  # 得到wrapper的地址
# res = test()  # 執行wrapper()
# print(res)  # => test的返回值，實際上是從wrapper()回傳過來的

# ------裝飾器的基本架構+返回值+有參數(3) = 裝飾器------
# import time
# def timmer(func):  # func = test
#     # def wrapper(name, age):  # 不能把參數寫死，因為每個函數參數不同
#     #     # print(func)
#     #     start = time.time()
#     #     res = func(name, age)  # 運行test()
#     #     end = time.time()
#     #     print("運行時間%s" % (end - start))
#     #     return res  # 因為實際上是執行wrapper()，所以要有返回值要從這return
#     def wrapper(*args, **kwargs):  # 不能把參數寫死，因為每個函數參數不同
#         # print(func)
#         start = time.time()
#         # args = ('jamie', 18, "man"), kwargs = {}，
#         # 所以要加*號，不然就會傳元組和字典過去，且能應付各種輸入
#         res = func(*args, **kwargs)
#         end = time.time()
#         print("運行時間%s" % (end - start))
#         return res  # 因為實際上是執行wrapper()，所以要有返回值要從這return
#     return wrapper
#
# @timmer   # @timmer 相當於 test = timmer(test)
# def test(name, age):
#     time.sleep(1)
#     print(name, age)  # => jamie 18
#     return "test的返回值"
# # test = timmer(test)  # 得到wrapper的地址
# res = test('jamie', 18)  # 執行wrapper()
# print(res)  # => test的返回值，實際上是從wrapper()回傳過來的
#
# @timmer
# def test_1(name, age, gender):
#     time.sleep(1)
#     print(name, age, gender)  # => jamie 18 man
#     return "test_1的返回值"
# res = test_1('jamie', 18, "man")  # 執行wrapper()
# print(res)  # => test_1的返回值，實際上是從wrapper()回傳過來的

# ------使用裝飾器模仿認證功能(1)------
# current = {'username': None, 'login': False}  # 要用來記錄帳戶是否登陸，這樣才不用每刷新頁面都要重登
# # 用戶清單
# user_list = [
#     {'name': "jamie", 'passwd': "123"},
#     {'name': "sb", 'passwd': "123"},
#     {'name': "nb", 'passwd': "123"}
# ]
# def auth_func(func):
#     def wrapper(*args, **kwargs):
#         if current["username"] and current["login"]:  # 已登入就直接進入頁面
#             res = func(*args, **kwargs)
#             return res
#         username = input("帳號 ").strip()
#         password = input("密碼 ").strip()
#         for user in user_list:  # for_else
#             if username == user["name"] and password == user["passwd"]:
#                 res = func(*args, **kwargs)
#                 current["username"] = username  # 第一次登陸成功後保持都登入狀態
#                 current["login"] = True
#                 return res
#         else:
#             print("帳號或密碼錯誤")
#     return wrapper
# @ auth_func
# def index():
#     print("歡迎來到主頁")
# @ auth_func
# def home(name):
#     print("%s~歡迎回家" % name)
# @ auth_func
# def shopping_car(name):
#     print("%s目前已選購 [%s, %s, %s]" % (name, "奶茶", "妹妹", "娃娃"))
#
# index()
# home("jamie")
# shopping_car("jamie")

# ------使用裝飾器(有參數)模仿認證功能(2)------
# current = {'username': None, 'login': False}  # 要用來記錄帳戶是否登陸，這樣才不用每刷新頁面都要重登
# # 用戶清單
# user_list = [
#     {'name': "jamie", 'passwd': "123"},
#     {'name': "sb", 'passwd': "123"},
#     {'name': "nb", 'passwd': "123"}
# ]
# def auth(auth_type = "local"):
#     def auth_func(func):
#         def wrapper(*args, **kwargs):
#             if auth_type == "local":
#                 print("資料類型是%s" % auth_type)
#                 if current["username"] and current["login"]:  # 已登入就直接進入頁面
#                     res = func(*args, **kwargs)
#                     return res
#                 username = input("帳號 ").strip()
#                 password = input("密碼 ").strip()
#                 for user in user_list:  # for_else
#                     if username == user["name"] and password == user["passwd"]:
#                         res = func(*args, **kwargs)
#                         current["username"] = username  # 第一次登陸成功後保持都登入狀態
#                         current["login"] = True
#                         return res
#                 else:
#                     print("帳號或密碼錯誤")
#             elif auth_type == "sql":
#                 print("資料類型是%s" % auth_type)
#         return wrapper
#     return auth_func
#
# # auth_func = auth(auth_type = "local") ---> @ auth_func(且附加了auth_type) ---> index = auth_func(index)
# @ auth()
# def index():
#     print("歡迎來到主頁")
# @ auth(auth_type = "sql")
# def home(name):
#     print("%s~歡迎回家" % name)
# @ auth(auth_type = "local")
# def shopping_car(name):
#     print("%s目前已選購 [%s, %s, %s]" % (name, "奶茶", "妹妹", "娃娃"))
#
# index()
# home("jamie")
# shopping_car("jamie")

# ------解壓序列------
# a, b, c = "yes"
# print(a)  # => y

# li = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# a, *_, b, c = li  # a為開頭，b為倒數第二，c為結尾，中間的*_代表用_代替中間所有值
# print(a)  # => 10
# print(_)  # => [9, 8, 7, 6, 5, 4, 3]
# print(b)  # => 2
# print(c)  # => 1

# a = 2
# b = 1
# b, a = a, b
# print(a, b)  # => 1 2
