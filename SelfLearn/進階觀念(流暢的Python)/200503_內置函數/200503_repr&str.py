"""
str()和repr()比較：
        一、str(object)將其轉化成為適於人閱讀的形式；repr(object)就是轉換成為閱讀器閱讀的形式。
        二、若對象內沒有設置 __str__ 函數，Python則會用 __repr__ 代替。
        三、__str__  在使用str()函數和使用print打印對象時會被調用；
                __repr__ 在使用repr()時和單獨使用對象被調用。
"""


# ----------終端顯示比較----------
text = "Hello World\n"

# 較適合機器去看
print(repr(text))
# 對人來說較友好
print(text)
print(str(text))


# ----------自定義函數----------
class Birthday:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    def __str__(self):
        return "str: {}/{}/{}".format(self.year, self.month, self.day)

    def __repr__(self):
        return "repr: {}-{}-{}".format(self.year, self.month, self.day)


obj = Birthday(1996, 1, 1)
# 會調用到__str__時機
print(obj)
print(str(obj))
print("%s" % obj)
# 會調用到__repr__時機
print(repr(obj))
print("%r" % obj)

