from multiprocessing import Process, Pool
import time, os

def Foo(i):
    time.sleep(1)
    print('sub ', i, os.getpid())
    return 'END %s' % i

# 回調函數用途：如果有很多進程最後都要做相同的事，那麼統一就可以交給主進程做，不用讓每個子進程個別執行
def Bar(arg):  # 參數為子進程return的值
    print('who ', os.getpid())  # 跟main pid相同
    print(arg)

if __name__ == '__main__':  # 一定要用，不然其他進程也會調用到
    print('main ', os.getpid())
    pool = Pool(5)  # 進程池對象，max=5
    #
    # Bar(1)
    # print("---------------- ")

    for i in range(20):
        # 用進程池開起進程
        # pool.apply(func=Foo, args=(i,))  # apply同步
        # pool.apply_async(func=Foo, args=(i,))  # apply_async異步

        # callback回調函數：就是某個動作(Foo)執行成功之後再去執行的動作(Bar)
        pool.apply_async(func=Foo, args=(i,), callback=Bar)  # callback是主進程調用的

    # 用進程池一定要先close再join，且缺一不可
    pool.close()
    pool.join()

    print('end all')