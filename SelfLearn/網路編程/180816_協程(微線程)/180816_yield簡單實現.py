import time

def consumer(name):
     print("--->ready to eat baozi... ")
     while True:
        new_baozi = yield
        print("[%s] is eating baozi %s " % (name, new_baozi))
        # time.sleep(1)

def producer():
    r = con. __next__ ()
    r = con2. __next__ ()
    n = 0
    while n < 10:
        time.sleep(1)
        print("\033[32;1m[producer]\033[0m is making baozi %s and %s" % (n, n+1))
        con.send(n)
        con2.send(n+1)
        n += 2

if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    producer()
