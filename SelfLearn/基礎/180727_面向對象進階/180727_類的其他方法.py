# __slots__(省內存，但會造成許多需要__dict__的方法不能使用)
# class Foo:
#     __slots__ = ['name', 'age']  # {'name': None, 'age': None}
#     # __slots__ = 'name'
#
# f1 = Foo()
# f1.name = 'jamie'
# print(f1.name)  # => jamie
#
# # f1.zzzzz = 18  # => error，因為新增要添加到__dict__中，但__slots__會取代掉__dict__
# # print(f1.__dict__)  # => __slots__取代掉__dict__
# print(f1.__slots__)  # => name
# print(Foo.__dict__)  # => 類還是可以使用__dict__，但創造出的實例會被限制不能使用__dict__


# __doc__(不會被繼承)
# class Foo:
#     'Foo'
#     pass
# class Bar(Foo):
#     pass
# print(Bar.__dict__)  # => {'__module__': '__main__', '__doc__': None}
# print(Foo.__dict__)
# # => {'__dict__': <attribute '__dict__' of 'Foo' objects>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__module__': '__main__', '__doc__': 'Foo'}


# __module__& __class__
# from module.aa import C
# c1 = C()
# print(c1.__module__)  # => module.aa
# print(c1.__class__)  # => <class 'module.aa.C'>


# __call__
# class Foo:
#     def __call__(self, *args, **kwargs):
#         print('執行__call__')
# f1 = Foo()
# f1()  # => 執行Foo下的__call__，有__call__對象才能加()

