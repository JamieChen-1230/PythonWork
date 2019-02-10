# 用getattr實現二次加工

import time
class Open:
    def __init__(self, filename, mode = 'r', encoding = 'utf-8'):
        self.filename = filename
        self.file = open(filename, mode, encoding=encoding)
        self.mode = mode
        self.encoding = encoding

    def write(self, s):
        self.file.write(time.asctime()+" "+s+"\n")

    def __getattr__(self, item):  # 不自定義方法就去抓原方法
        print(item, type(item))
        return getattr(self.file, item)  # self.file是文件對象，抓取文件對象的相對應方法

f1 = Open('a.txt', 'w+')
# print(f1.file)  # => <_io.TextIOWrapper name='a.txt' mode='w' encoding='utf-8'>
# f1.file.write("11")
# print(f1.read)  # => <built-in method read of _io.TextIOWrapper object at 0x000001552A4CEB40>
f1.write("1")
f1.write("2")
f1.seek(0)
print(f1.read())
