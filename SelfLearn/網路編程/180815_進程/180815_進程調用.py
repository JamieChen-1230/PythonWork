# 由於GIL的存在，python中的多線程其實並不是真正的多線程，
# 如果想要充分地使用多核CPU的資源，在python中大部分情況需要使用多進程

# -------調用方法一-------
# import multiprocessing
# import time
#
#
# def f(name):
#     time.sleep(1)
#     print('hello', name, time.ctime())
#
# if __name__ == '__main__':
#     p_list = []
#     for i in range(3):
#         # 併行
#         p = multiprocessing.Process(target=f, args=('alvin',))
#         p_list.append(p)
#         p.start()
#     for i in p_list:
#         i.join()
#     print('end')

# -------調用方法二-------
# from multiprocessing import Process
# import time, random
#
# class MyProcess(Process):
#     def __init__ (self):
#         super(MyProcess, self). __init__ ()
#         # self.name = name
#     def run(self):
#         time.sleep(1)
#         print('hello', self.name, time.ctime())
#
# if __name__ == '__main__':
#     p_list = []
#     for i in range(3):
#         p = MyProcess()
#         # p.daemon = True  # 守護進程
#         p.start()
#         p_list.append(p)
#
#     for p in p_list:
#         p.join()
#
#     print('end')



