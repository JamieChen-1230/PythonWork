class Mytype(type):
    def __init__(self, a, b, c):
        print('自定義元類')
        # print(a)  # => Foo
        # print(b)  # => ()
        # print(c)  # => {'__module__': '__main__', '__init__': <function Foo.__init__ at 0x00000205A2855598>, '__qualname__': 'Foo'}

    def __call__(self, *args, **kwargs):
        # print(self)  # => <class '__main__.Foo'>
        # print(args, kwargs)  # => ('jamie',) {}
        obj = object.__new__(self)  # object.__new__(Foo) --> f1
        print(obj)
        self.__init__(obj, *args, **kwargs)
        return obj

class Foo(metaclass=Mytype):  # Foo = Mytype('Foo', (), {}) 加上self共4個參數
    def __init__(self, name):
        self.name = name


f1 = Foo('jamie')  # Foo+()會執行Foo的類的call方法
# print(f1)
print(f1.__dict__)