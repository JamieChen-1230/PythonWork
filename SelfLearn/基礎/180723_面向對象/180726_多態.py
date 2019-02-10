# 多態的概念：不同的類實例化出來的對象可以調用同一種方法

# s = str("jamie")  # 相當於str類實例化出了s
# # print(s)
# li = list("jamie")  # 相當於list類實例化出了li
# # print(li)
# # 且二者都能調用len()
# print(len(s))
# print(len(li))
# # .__len__()等同於len()
# print(s.__len__())
# print(li.__len__())

# class H2O:
#     def __init__(self, name, temperature):
#         self.name = name
#         self.temperature = temperature
#
#     def turn(self):
#         if self.temperature < 0:
#             print("%s 結冰了" % self.name)
#         elif self.temperature > 0 and self.temperature < 100:
#             print("%s 變成水了" % self.name)
#         elif self.temperature > 100:
#             print("%s 變成蒸氣了" % self.name)
# class Water(H2O):
#     pass
# class Ice(H2O):
#     pass
# class Steam(H2O):
#     pass
#
# w1 = Water("水", 25)
# i1 = Ice("冰", -20)
# s1 = Steam("氣", 200)
# # 不同類的對象(w1, s1, i1)調用相同方法(turn)
# w1.turn()  # => 水 變成水了
# i1.turn()  # => 冰 結冰了
# s1.turn()  # => 氣 變成蒸氣了
#
#
# # 模仿len()方法
# def func(obj):
#     obj.turn()
# func(w1)  # => 水 變成水了
