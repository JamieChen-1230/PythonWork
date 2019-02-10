import time
import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 6667))
sk.listen(5)
sk.setblocking(False)  # 默認是True阻塞I/O

while True:
    try:
        print('waiting client connection ....... ')
        connection, address = sk.accept()    # 進程主動輪詢，若無連接程序不會卡在這，則會報錯
        print("+++ ", address)
        client_messge = connection.recv(1024)
        print(str(client_messge, 'utf8'))
        connection.close()
    except Exception as e:
        print(e)
        time.sleep(4)  # 每隔4s去察看一次
