# 靜態屬性
# class Room:
#     def __init__(self, name, owner, width, length, heigh):
#         self.name = name
#         self.owner = owner
#         self.width = width
#         self.length = length
#         self.heigh = heigh
#
#     @property  # 靜態屬性，加上這個之後調用方法就不用加()
#     def area(self):  # self可以訪問實例屬性也可訪問類屬性
#         return self.width*self.length
#
# r1 = Room("套房", "jamie", 100, 100, 10)
# print("%s的%s總面積是%s" % (r1.owner, r1.name, r1.area))  # r1.area不用加()


#  類方法
# class Room:
#     tag = 1
#     def __init__(self, name, owner, width, length, heigh):
#         self.name = name
#         self.owner = owner
#         self.width = width
#         self.length = length
#         self.heigh = heigh
#
#     @property  # 封裝邏輯，加上這個之後調用方法就不用加()
#     def area(self):  # self可以訪問實例屬性也可訪問類屬性
#         return self.width*self.length
#
#     @classmethod  # 類在調用方法時使用，跟實例無關
#     def info(cls):  # 接收的是一個類名(cls)，只能訪問類屬性
#         print(cls.tag)  # => 1
#
# Room.info()  # 這樣即可調用info方法(類方法的定義是為了能直接用類去調用)


# 靜態方法：只是名義上的歸屬類管理
# class Room:
#     tag = 1
#     def __init__(self, name, owner, width, length, heigh):
#         self.name = name
#         self.owner = owner
#         self.width = width
#         self.length = length
#         self.heigh = heigh
#
#     @property  # 封裝邏輯，加上這個之後調用方法就不用加()
#     def area(self):  #  self可以訪問實例屬性也可訪問類屬性
#         return self.width*self.length
#
#     @classmethod  # 類在調用方法時使用，跟實例無關
#     def info(cls):  # 接收的是一個類名(cls)，只能訪問類屬性
#         print(cls.tag)  # => 1
#
#     @staticmethod   # 類的工具包，不跟實例和類綁定
#     def wash(a, b, c):  # 不能使用類屬性或實例屬性
#         print('%s %s %s正在洗澡' % (a, b, c))
#
# Room.wash(1, 2, 3)

