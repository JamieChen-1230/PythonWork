# li = list('jamie')
# print(li)  # =>['j', 'a', 'm', 'i', 'e']
#
# f = open("a.txt", 'w')
# print(f)  # => <_io.TextIOWrapper name='a.text' mode='w' encoding='cp950'>
#
# class Foo:
#     pass
# f1 = Foo()
# print(f1)  # => <__main__.Foo object at 0x000002DA0F549240>


# __str__
# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return '名字為%s' % self.name  # 回傳值必須為字符串
#
# f1 = Foo('jamie', 20)
# print(f1)  # => 名字為jamie

# __repr__
# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return '名字為%s' % self.name  # 回傳值必須為字符串
#
# f1 = Foo('jamie', 20)
# print(f1)  # => 名字為jamie
# f1.__str__() ------> f1.__repr__()，str與repr共存時，優先執行str
