from socket import *
import struct

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 100

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    msg = input('>>> ').strip()
    if not msg: continue
    if msg == 'break': break
    tcp_client.send(msg.encode('utf-8'))

    data = tcp_client.recv(buffer_size)
    print("收到服務端信息", data)
tcp_client.close()