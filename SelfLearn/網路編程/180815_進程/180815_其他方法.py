# ----------其他方法----------
# 實例方法：
# 　　is_alive()：返回進程是否在運行。
# 　　join([timeout])：阻塞當前上下文環境的進程程，直到調用此方法的進程終止或到達指定的timeout（可選參數）。
# 　　start()：進程準備就緒，等待CPU調度
# 　　run()：strat()調用run方法，如果實例進程時未制定傳入target，這star執行t默認run()方法。
# 　　terminate()：不管任務是否完成，立即停止工作進程
# 屬性：
# 　　daemon：和線程的setDeamon功能一樣
# 　　name：進程名字。
# 　　pid：進程號

import time
from multiprocessing import Process

class Myprocess(Process):
    def __init__(self, num):
        Process.__init__(self)
        self.num = num

    def run(self):
        time.sleep(1)
        print(self.is_alive(), self.num, self.pid)
        time.sleep(1)

if __name__ == '__main__':
    p_list = []
    for i in range(10):
        p = Myprocess(i)
        # p.daemon=True
        p_list.append(p)

    for p in p_list:
        p.start()
    # for p in p_list:
    #      p.join()

    print('main process end')