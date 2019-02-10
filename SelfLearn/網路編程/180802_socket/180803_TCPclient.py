# import socket
#
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# phone.connect(('127.0.0.1', 8000))  # 建立連結，三次交握
#
# phone.send('hello'.encode('utf-8'))  # 發消息，數據須為字節
#
# data = phone.recv(1024)
# print('收到服務端的消息: ', data)
#
# phone.close()


from socket import *

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)  # 創建socket客戶端
tcp_client.connect(ip_port)  # 嘗試連結服務器

while True:  # 通訊循環
    msg = input('>>> ').strip()
    if not msg: continue
    tcp_client.send(msg.encode('utf-8'))
    data = tcp_client.recv(buffer_size)
    print('服務端發來的信息 ', data.decode('utf-8'))

tcp_client.close()
