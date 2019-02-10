import threading, time


class Boss(threading.Thread):
     def run(self):
        print("BOSS：今晚大家都要加班到22:00。")
        print(event.isSet())  # => False，判斷event是否被設定
        event.set()
        time.sleep(5)
        print("BOSS：<22:00>可以下班了。")
        print(event.isSet())
        event.set()

class Worker(threading.Thread):
     def run(self):
        event.wait()  # 一旦event被set，等同於pass
        print("Worker：哎……命苦啊！")
        time.sleep(1)
        event.clear()  # 把上一次的event清空
        event.wait()   # 再次等待被set
        print("Worker：OhYeah!")

if __name__ == "__main__":
    event = threading.Event()
    threads = []
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print('end')