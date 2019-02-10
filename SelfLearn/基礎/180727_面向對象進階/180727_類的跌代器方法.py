# import time
# class Foo:
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.n += 1
#         time.sleep(0.1)
#         if self.n == 10:
#             raise StopIteration('終止了')
#         return self.n
#
# f1 = Foo(1)
#
# for i in f1:  # for在循環前會先執行 對象.__iter__() ------> f1.__iter__
#     # 每次循環調用__next__()，直到發生StopIteration異常
#     print(i)


# 實現斐波那契數列
class Fib:
    def __init__(self):  # 起始兩個值
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration("結束")
        return self.a

f1 = Fib()
for i in f1:
    print(i)
