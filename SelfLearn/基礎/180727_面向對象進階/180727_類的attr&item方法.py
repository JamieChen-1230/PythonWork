# ------------attr------------
# class Foo:
#     x = 1
#     def __init__(self, y):
#         self.y = y
#
#     def __getattr__(self, item):
#         print("執行__getattr__")
#
# f1 = Foo(10)
# print(f1.y)
# print(getattr(f1, 'y'))
#
# f1.sssssss  # => 執行__getattr__，當調用不存在的方法時會觸發__getattr__

# class Foo:
#     x = 1
#     def __init__(self, y):
#         self.y = y
#
#     def __getattr__(self, item):
#         print("執行__getattr__")
#
#     def __getattribute__(self, item):
#         print("執行__getattribute__")
#         raise AttributeError("有異常了")  # 自定義發生AttributeError異常，再發生AttributeError異常的同時會觸發__getattr__
#
# f1 = Foo(10)
# # 有沒有存在該屬性都會觸發__getattribute__
# # f1.x  # => 執行__getattribute__
# f1.xxxxxx  # => 執行__getattribute__

# class Foo:
#     x = 1
#     def __init__(self, y):
#         self.y = y
#
#     def __delattr__(self, item):
#         print("執行__delattr__")
#
# f1 = Foo(10)
# del f1.y  # => 執行__delattr__，當進行刪除動作時會被調用
# del f1.x  # => 執行__delattr__


# class Foo:
#     x = 1
#     def __init__(self, y):
#         self.y = y
#
#     def __setattr__(self, key, value):
#         print("執行__setattr__")
#         # self.key = value ，這等同於設置屬性，所以又會觸發__setattr__，造成死循環
#         self.__dict__[key] = value  # 會把我們設置的屬性加入__dict__
#
# f1 = Foo(10)  # => 執行__setattr__，設置屬性就會觸發(__init__也算)
# f1.z = 2  # => 執行__setattr__

# 我們可以自定義這些方法
# class Foo:
#     x = 1
#     def __init__(self, y):
#         self.y = y
#
#     def __getattr__(self, item):
#         print("執行__getattr__，你找的屬性 %s 並不存在" % item)
#
#     def __setattr__(self, key, value):
#         print("執行__setattr__，你設置了屬性 %s=%s" % (key, value))
#
#     def __delattr__(self, item):
#         print("執行__delattr__，刪除 %s" % item)
#
# f1 = Foo(10)  # => 執行__setattr__，你設置了屬性 y=10
# print(f1.__dict__)  # => {}，沒有添加(因為__setattr__被我們給覆蓋掉了)
# f1.z  # => 執行__getattr__，你找的屬性 z 並不存在
# del f1.y


# ------------item------------
# 跟attr功能相同，只是調用方法不同
# class Foo:
#     def __getitem__(self, item):
#         print("執行__getitem__，你找的屬性 %s " % item)
#         return self.__dict__
#
#     def __setitem__(self, key, value):
#         print("執行__setitem__，你設置了屬性 %s=%s" % (key, value))
#         self.__dict__[key] = value
#
#     def __delitem__(self, item):
#         print("執行__delitem__，刪除 %s" % item)
#         self.__dict__.pop(item)
#
# f1 = Foo()
# f1['name']
# f1['name'] = 'jamie'
# print(f1.__dict__)
# del f1['name']
# print(f1.__dict__)

