# 同步鎖造成的副作用

# -----------造成死鎖-----------
# import threading, time
#
# class Mythread(threading.Thread):
#
#     def actionA(self):
#         A.acquire()
#         print(self.name, 'got A at', time.ctime())
#         time.sleep(2)
#
#         B.acquire()
#         print(self.name, 'got B at', time.ctime())
#         time.sleep(1)
#         B.release()
#
#         A.release()
#
#     def actionB(self):
#         B.acquire()
#         print(self.name, 'got B at', time.ctime())
#         time.sleep(2)
#
#         A.acquire()
#         print(self.name, 'got A at', time.ctime())
#         time.sleep(1)
#         A.release()
#
#         B.release()
#
#     def run(self):
#         self.actionA()
#         self.actionB()
#
#
#
#
# if __name__ == '__main__':
#     A = threading.Lock()
#     B = threading.Lock()
#
#     l = []
#     for i in range(5):
#         t = Mythread()
#         t.start()
#         l.append(t)
#
#     for i in l:
#         i.join()
#
#     print('end')


# -----------用遞歸鎖解決死鎖-----------
import threading, time

class Mythread(threading.Thread):
    def actionA(self):
        r_lock.acquire()
        print(self.name, 'got A at', time.ctime())
        time.sleep(2)

        r_lock.acquire()
        print(self.name, 'got B at', time.ctime())
        time.sleep(1)
        r_lock.release()

        r_lock.release()

    def actionB(self):
        r_lock.acquire()
        print(self.name, 'got B at', time.ctime())
        time.sleep(2)

        r_lock.acquire()
        print(self.name, 'got A at', time.ctime())
        time.sleep(1)
        r_lock.release()

        r_lock.release()

    def run(self):
        self.actionA()
        self.actionB()


if __name__ == '__main__':
    # A = threading.Lock()
    # B = threading.Lock()

    r_lock = threading._RLock()  # 遞歸鎖

    l = []
    for i in range(5):
        t = Mythread()
        t.start()
        l.append(t)

    for i in l:
        i.join()

    print('end')