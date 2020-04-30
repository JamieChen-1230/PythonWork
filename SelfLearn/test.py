# # class Foo:
# #     def f(self):
# #         # f1()
# #         self.f1()
# #     def f1(self):
# #         print('f1')
# #     # def f2():
# #     #     print('f2')
# # ff = Foo()
# # ff.f()
# # # Foo.f2()
# import datetime
# today = datetime.datetime.now()
# today_str = today.strftime("%Y-%m-%d")
# before_7days = today - datetime.timedelta(7)
# before_7days_str = before_7days.strftime("%Y-%m-%d")
# print("before_7days_str", before_7days_str)



# def f1(a, b):
#     ab = a + b
#     def f2(c):
#         abc = ab * c
#         return abc
#     return f2
#
# print(f1(2,3)(4))

