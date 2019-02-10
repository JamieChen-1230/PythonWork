# udp的recvfrom是阻塞的，
# 一個recvfrom(x)必須對唯一一個sendinto(y),收完了x個字節的數據就算完成,若是y>x數據就丟失，
# 這意味著udp根本不會粘包，但是會丟數據，不可靠
from socket import *

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)  # 創建socket服務器
udp_server.bind(ip_port)  # 將地址綁到服務器

# UDP一個recvfrom對應一個sendto
data1 = udp_server.recvfrom(buffer_size)
print('第一次接收數據 ', data1)
data2 = udp_server.recvfrom(buffer_size)
print('第二次接收數據 ', data2)
data3 = udp_server.recvfrom(buffer_size)
print('第三次接收數據 ', data3)


udp_server.close()