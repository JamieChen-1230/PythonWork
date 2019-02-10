import threading  # 線程
import time

def hi(num):
    print('hello %s' % num)
    time.sleep(2)
    print('bye %s' % num)

if __name__ == '__main__':
    # hi(10)
    # hi(9)
    t1 = threading.Thread(target=hi, args=(10,))  # 創建一個線程對象t1
    t1.start()  # 執行hi(10)
    t2 = threading.Thread(target=hi, args=(9,))  # 創建一個線程對象t2
    t2.start()  # 執行hi(9)

    print('end')  # 主線程

