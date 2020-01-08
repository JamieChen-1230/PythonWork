class A:
    def test(self):
        print("A")

class B(A):
    # def test(self):
    #     print("B")
    pass

class C(A):
    def test(self):
        print("C")

class D(B):
    # def test(self):
    #     print("D")
    pass

class E(C):
    def test(self):
        print("E")

class F(D, E):
    # def test(self):
    #     print("F")
    pass

f1 = F()
f1.test()  # 尋找順序：F ---> D ---> B ---> E ---> C ---> A ---> 沒找到test()
# __mro__屬性 => 依照方法解析順序列出各個超類
print(F.__mro__)
# => (<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
