# def deco(obj):
#     print("---------------", obj)
#     obj.x = 1
#     return obj
#
# # @deco   # test = deco(test)
# # def test():
# #     print("test")
#
# @deco   # Foo = deco(Foo)
# class Foo:
#     pass
#
# print(Foo.__dict__)


# def typed(**kwargs):
#     def deco(obj):
#         print('deco', kwargs)
#         print("---------------", obj)
#         # obj.x = kwargs['x']
#         # obj.y = kwargs['y']
#         # obj.z = kwargs['z']
#         for k, v in kwargs.items():
#             setattr(obj, k, v)
#         return obj
#     print(kwargs)
#     return deco
#
# @typed(x=1, y=2, z=3)   # @typed(x=1, y=2, z=3) ----> @deco ----> Foo = deco(Foo)
# class Foo:
#     pass
#
# print(Foo.__dict__)


# 類的裝飾器的應用
# class Typed:
#     def __init__(self, key, expected_type):
#         self.key = key
#         self.expected_type = expected_type
#     def __get__(self, instance, owner):
#         print('get')
#         return instance.__dict__[self.key]
#     def __set__(self, instance, value):
#         print('set')
#         if not type(value) is self.expected_type:
#             raise TypeError("%s 數據類型須為 %s" % (self.key, self.expected_type))
#         instance.__dict__[self.key] = value
#     def __delete__(self, instance):
#         print('delete')
#         instance.__dict__.pop(self.key)
#
#
# def deco(**kwargs):  # kwargs = {name: str, age: int, salary: float}
#     def wrapper(obj):
#         for k, v in kwargs.items():  # ((name, str), (age, int), (salary, float))
#             setattr(obj, k, Typed(k, v))
#             # setattr(People, 'name', Type('name', str)) ---> People.name = Type('name', str)
#         return obj
#     print(kwargs)
#     return wrapper
#
#
# @ deco(name=str, age=int, salary=float)  # @deco ---> wrapper ----> People = wrapper(People)
# class People:
#     # name = Typed('name', str)
#     # age = Typed('age', int)
#     # salary = Typed('salary', float)
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
# p1 = People('jamie', 21, 2.2)
# print(p1.__dict__)


