from socket import *

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)  # 創建socket客戶端

udp_client.sendto('hello'.encode('utf-8'), ip_port)
udp_client.sendto('world'.encode('utf-8'), ip_port)
udp_client.sendto('jamie'.encode('utf-8'), ip_port)


udp_client.close()
