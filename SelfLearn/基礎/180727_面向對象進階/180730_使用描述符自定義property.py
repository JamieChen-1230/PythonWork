# class Room:
#     def __init__(self, name, width, length):
#         self.name = name
#         self.width = width
#         self.length = length
#
#     @property  # area = property(area)
#     def area(self):
#         return self.width * self.length
#
# r1 = Room('廁所', 10, 10)
# print(r1.area)  # => 100
# print(Room.__dict__)  # 'area': <property object at 0x000001C629AA0AE8>


# 自定義property + 延遲計算 (非數據描述符)
# class Myproperty:  # 1
#     def __init__(self, func):  # 2, 7(self=area, func=Room裡的area方法)
#         self.func = func  # 8
#         print(func)  # <function Room.area at 0x00000150273457B8> # 9
#
#     def __get__(self, instance, owner):  # 3, 16(self=Myproperty實例area)
#         print('get', instance, owner)  # instance = r1  # 17
#         if instance is None:  # 18
#             return self
#         res = self.func(instance)
#         setattr(instance, self.func.__name__, res)  # 把結果存在r1的dict中，下次調用會直接從實例屬性字典裡找(延遲計算)
#         return res  # 19(self.func(instance) = Myproperty實例area.Room裡的area(r1))
#
#
# class Room:  # 4
#     def __init__(self, name, width, length):  # 5, 11(self=r1)
#         self.name = name  # 12
#         self.width = width  # 13
#         self.length = length  # 14
#
#     @Myproperty  # area = Myproperty(area)  # 6(調用Myproperty(area)，並定義成一個描述符)
#     def area(self):  # 20
#         return self.width * self.length  # 21
#
# r1 = Room('廁所', 10, 10)  # 10(建立Room實例r1)
# print(r1.area)  # 15(調用到area描述符)
# print(r1.__dict__)
# print(r1.area)  # 會直接從實例字典裡調用


# 自定義property + 延遲計算 (數據描述符)
# class Myproperty:  # 1
#     def __init__(self, func):  # 2, 7(self=area, func=Room裡的area方法)
#         self.func = func  # 8
#         print(func)  # <function Room.area at 0x00000150273457B8> # 9
#
#     def __get__(self, instance, owner):  # 3, 16(self=Myproperty實例area)
#         print('get', instance, owner)  # instance = r1  # 17
#         if instance is None:  # 18
#             return self
#         res = self.func(instance)
#         setattr(instance, self.func.__name__, res)
#         return res  # 19(self.func(instance) = Myproperty實例area.Room裡的area(r1))
#
#     def __set__(self, instance, value):
#         pass
#
#
# class Room:  # 4
#     def __init__(self, name, width, length):  # 5, 11(self=r1)
#         self.name = name  # 12
#         self.width = width  # 13
#         self.length = length  # 14
#
#     @Myproperty  # area = Myproperty(area)  # 6(調用Myproperty(area)，並定義成一個描述符)
#     def area(self):  # 20
#         return self.width * self.length  # 21
#
# r1 = Room('廁所', 10, 10)  # 10(建立Room實例r1)
# print(r1.area)  # 15(調用到area描述符)
# print(r1.__dict__)
# print(r1.area)  # 還是會從get那去找，而不是從實例字典裡找(因為數據描述符 > 實例屬性)


