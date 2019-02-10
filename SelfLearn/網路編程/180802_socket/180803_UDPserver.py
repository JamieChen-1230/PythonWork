# udp的recvfrom是阻塞的，
# 一個recvfrom(x)必須對唯一一個sendinto(y),收完了x個字節的數據就算完成,若是y>x數據就丟失，
# 這意味著udp根本不會粘包，但是會丟數據，不可靠

from socket import *

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)  # SOCK_DGRAM基於UDP協議
udp_server.bind(ip_port)  # 將地址綁到服務器

while True:
    data, addr = udp_server.recvfrom(buffer_size)
    print('客戶端發來的信息 ', data)
    udp_server.sendto(data.upper(), addr)
