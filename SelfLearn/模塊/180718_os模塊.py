# ---------os模塊---------
import os
# os.getcwd() 獲取當前目錄絕對路徑
# print(os.getcwd())  # => D:\PythonWork\SelfLearn\基礎

# os.chdir() 變換當前工作目錄
# print(os.getcwd())  # => D:\PythonWork\SelfLearn\基礎
# os.chdir("180715_模塊基本架構介紹")
# print(os.getcwd())  # => D:\PythonWork\SelfLearn\基礎\180715_模塊基本架構介紹
# print(os.getcwd())  # => D:\PythonWork\SelfLearn\基礎\180715_模塊基本架構介紹
# os.chdir("..")  # 上一層
# print(os.getcwd())  # => D:\PythonWork\SelfLearn\基礎

# os.makedirs() 建立資料夾
# os.makedirs("test1/test2")

# os.removedirs() 刪除資料夾(只能刪除空資料夾)
# os.removedirs("test1/test2")  # test1,2都刪了

# os.listdir() 找出當前目錄的所有文件
# print(os.listdir())

# os.remove() 刪除一個文件
# os.remove("a.txt")

# os.rename() 改名稱
# os.rename("a.txt", "b.txt")

# os.stat() 查看檔案資訊
# print(os.stat("180718_Python內建模塊.py"))  # size字節數, atime最近查看文件時間, mtime最近修改時間, ctime創建時間

# os.sep 當前環境的路徑分隔符
# print(os.sep)  # => \

# os.system() 執行一個系統命令
# os.system("dir")

# os.path.abspath() 獲取文件絕對路徑
# print(os.path.abspath("180718_Python內建模塊.py"))  # => D:\PythonWork\SelfLearn\基礎\180718_Python內建模塊.py

# os.path.split() 將路徑分割為目錄和文件
# print(os.path.split(os.path.abspath("180718_Python內建模塊.py")))
# # => ('D:\\PythonWork\\SelfLearn\\基礎', '180718_Python內建模塊.py')

# os.path.dirname() 找出路徑中的目錄，也就是os.path.split()的第一元素
# print(os.path.dirname(os.path.abspath("180718_Python內建模塊.py")))  # => D:\PythonWork\SelfLearn\基礎

# os.path.basename() 找出路徑中的文件名，也就是os.path.split()的第二元素
# print(os.path.basename(os.path.abspath("180718_Python內建模塊.py")))  # => 180718_Python內建模塊.py

# os.path.exists() 判斷路徑是否存在
# print(os.path.exists("180718_Python內建模塊.py"))  # => True
# print(os.path.exists("基礎"))  # => False
# print(os.path.exists("D:/PythonWork/SelfLearn/基礎"))  # => True

# os.path.isfile() 判斷是否是存在的文件
# print(os.path.isfile("180718_Python內建模塊.py"))  # => True
# print(os.path.isfile("D:/PythonWork/SelfLearn/基礎/180718_Python內建模塊.py"))  # => True
# print(os.path.isfile("D:/PythonWork/SelfLearn/基礎"))  # => False

# os.path.isdir() 判斷是否是存在的目錄
# print(os.path.isdir("D:/PythonWork/SelfLearn/基礎/180718_Python內建模塊.py"))  # => False
# print(os.path.isdir("D:/PythonWork/SelfLearn/基礎"))  # => True

# (*重要)os.path.join() 路徑拼接
# a = "D:/PythonWork/SelfLearn"
# b = "基礎/180718_Python內建模塊.py"
# print(os.path.join(a, b))  # => D:/PythonWork/SelfLearn\基礎/180718_Python內建模塊.py
# print(os.path.exists("D:/PythonWork/SelfLearn\基礎/180718_Python內建模塊.py"))  # => True

# 得到進程編號
# print(os.getppid())  # 父進程
# print(os.getpid())   # 本身進程
