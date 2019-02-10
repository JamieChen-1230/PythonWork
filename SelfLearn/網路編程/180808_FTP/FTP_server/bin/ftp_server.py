# 為啟動文件
import os, sys
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(PATH)  # => D:\PythonWork\SelfLearn\網路編程\180808_FTP\FTP_server
sys.path.append(PATH)

from module import main

if __name__ == '__main__':
    main.ArgvHandler()
