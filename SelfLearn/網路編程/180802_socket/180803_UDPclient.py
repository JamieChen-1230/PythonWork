# udp的recvfrom是阻塞的，
# 一個recvfrom(x)必須對唯一一個sendinto(y),收完了x個字節的數據就算完成,若是y>x數據就丟失，
# 這意味著udp根本不會粘包，但是會丟數據，不可靠
from socket import *

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('>>> ').strip()
    udp_client.sendto(msg.encode('utf-8'), ip_port)  # UDP無鏈結，只能send時決定發給誰
    data, addr = udp_client.recvfrom(buffer_size)
    print('服務端發來的信息 ', data)