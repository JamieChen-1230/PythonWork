from multiprocessing import Process
import os
import time

# 程序主進程的父進程是Pycharm的PID
def info(title):
    print("title: ", title)
    print('parent process: ', os.getppid())  # 父進程
    print('process id: ', os.getpid())   # 本身進程

def f(name):
    info('function f ')
    print('hello ', name)


if __name__ == '__main__':
    info('main process line')
    time.sleep(1)
    print("------------------")
    p = Process(target=info, args=('yuan',))
    p.start()
    p.join()
