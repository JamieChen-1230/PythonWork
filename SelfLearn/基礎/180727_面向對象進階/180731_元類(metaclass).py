# 元類就是類的類，元類的實例是類，類的實例是對象
# type是python內建元類

# class Foo:
#     pass
#
# f1 = Foo()
# print(type(f1))  # => <class '__main__.Foo'>
# print(type(Foo))  # => <class 'type'>，類是由type產生的


# class Foo:
#     pass
# print(Foo)  # => <class '__main__.Foo'>
#
# FFo = type('FFo', (object,), {'x': 1})
# print(FFo)  # => <class '__main__.FFo'>


# 用type實例化一個類
# def __init__(self, name):
#     self.name = name
#
# FFo = type('FFo', (object,), {'x': 1, '__init__':__init__})
# print(FFo)  # => <class '__main__.FFo'>
# print(FFo.__dict__)
# f1 = FFo('jamie')
# print(f1.name)  # => jamie
