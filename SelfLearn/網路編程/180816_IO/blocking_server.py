import time
import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 6667))
sk.listen(5)

print('waiting client connection ....... ')
while True:
    connection, address = sk.accept()    # 若無連接程序會卡在這
    print("+++ ", address)
    client_messge = connection.recv(1024)
    print(str(client_messge, 'utf8'))
    connection.close()

