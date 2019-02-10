# 信號量也是同步的

import threading, time

class myThread(threading.Thread):
     def run(self):
         if semaphore.acquire():  # 有五把鑰匙
             print(self.name)
             time.sleep(5)
             semaphore.release()  # 把鎖釋放

if __name__ == "__main__" :
    semaphore = threading.Semaphore(5)  # 信號鎖，設定同時能有幾個線程使用
    thrs = []
    for i in range(100):
        thrs.append(myThread())
    for t in thrs:
        t.start()
