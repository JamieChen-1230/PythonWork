# UDP無連結

from socket import *
import time

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM基於UDP協議
udp_server.bind(ip_port)  # 將地址綁到服務器

while True:
    data, addr = udp_server.recvfrom(buffer_size)
    print('客戶端發來的信息 ', data)
    if not data:
        fmt = '%Y-%m-%d %X'
    else:
        fmt = data.decode('utf-8')

    back_time = time.strftime(fmt)
    udp_server.sendto(back_time.encode('utf-8'), addr)