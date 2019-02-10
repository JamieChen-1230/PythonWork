# 一個類中至少會實現__get__(), __set__(), __delete__()中的一個，這也被稱為描述符協議
# 描述符：用來代理另一個類的屬性(必須把描述符定義成這個類的類屬性，不能定義在init裡)
# __get__() 調用一個屬性時觸發
# __set__() 為一個屬性賦值時觸發
# __delete__() 採用del刪除屬性時觸發

# class Foo:
#     def __get__(self, instance, owner):
#         print("get")
#
#     def __set__(self, instance, value):
#         print("set")
#
#     def __delete__(self, instance):
#         print('delete')
#
#
# class Bar:
#     x = Foo()
#     def __init__(self, n):
#         self.x = n
#
# b1 = Bar(10)  # 觸發Foo()的__set__()，因為x已經成為Foo()的代理人
# print(b1.__dict__)  # => {}
# # b1.x = 8787   # 觸發Foo()的__set__()
# b1.y = 100  # y不是代理人，所以這只是單純的新增屬性
# print(b1.__dict__)  # {'y': 100}


# class Foo:
#     def __get__(self, instance, owner):
#         print("get")
#
#     def __set__(self, instance, value):
#         print("set", instance, value)  # instance = b1
#         instance.__dict__['x'] = value  # 在b1.__dict__['x']添加值
#
#     def __delete__(self, instance):
#         print('delete')
#
#
# class Bar:
#     x = Foo()  # x為Foo()的代理人
#     def __init__(self, n):
#         self.x = n  # b1.x = n，因為x是Foo()的代理對象，所以會調用到Foo()裡的方法
#
# b1 = Bar(10)  # 觸發Foo()的__set__()，因為x已經成為Foo()的代理人
# print(b1.__dict__)  # => {'x': 10}


# 描述符優先級
# 類屬性 > 數據描述符(至少有get, set) > 實例屬性 > 非數據描述符(沒有set) > __getattr__
# class Foo:
#     def __get__(self, instance, owner):
#         print("get")
#
#     def __set__(self, instance, value):
#         print("set")
#
#     def __delete__(self, instance):
#         print('delete')
#
#
# class Bar:
#     x = Foo()
#
# # print(Bar.x)  # 觸發__get__
#
# # Bar.x = 1  # 不會觸發__set__，因為類屬性 > 數據描述符，所以x會被覆蓋
# # print(Bar.x)  # => 1
#
# # 因為數據描述符 > 實例屬性
# # b1 = Bar()
# # b1.x  # 觸發__get__
# # b1.x = 1  # 觸發__set__
# # del b1.x  # 觸發__delete__


# 描述符的應用
# python為弱類型語言，不會限制變量數據類型
# class Typed:
#     def __init__(self, key, expected_type):
#         self.key = key
#         self.expected_type = expected_type
#     def __get__(self, instance, owner):
#         print('get')
#         # print(instance, owner)
#         return instance.__dict__[self.key]
#     def __set__(self, instance, value):
#         print('set')
#         # print(instance, value)
#         if not type(value) is self.expected_type:
#             # print("nnnnnn")
#             # return
#             raise TypeError("%s 數據類型須為 %s" % (self.key, self.expected_type))
#         instance.__dict__[self.key] = value
#     def __delete__(self, instance):
#         print('delete')
#         # print(instance)
#         instance.__dict__.pop(self.key)
#
# class People:
#     name = Typed('name', str)
#     age = Typed('age', int)
#     salary = Typed('salary', float)
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
# # p1 = People('jamie', 21, 2.2)
# # print(p1.__dict__)
# print(People.__dict__)
