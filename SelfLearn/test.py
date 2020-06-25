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



# di = {'a': 1, 'b': 2}
# print(id(di))
# di['a'] = 10
# print(di, id(di))



import numpy

a = numpy.array([1, 2])
print(a, id(a))
a[0] = 3
print(a, id(a))


# import array
#
# b = array.array('d', [1, 'a'])
# print(b)

