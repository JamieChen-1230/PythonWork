# li = ['a', 'b', 'c', 'd']
#
# def test():
#     return li.pop()
#
# for i in iter(test, 'b'):  #  執行到'b'為止
#     print(i)
#
# # d
# # c


from functools import partialf
def add(x,y):
    return x+y
func = partial(add, 1)  # 固定add的第一個參數為1
print(func(1))  # => 2
print(func(2))  # => 3
