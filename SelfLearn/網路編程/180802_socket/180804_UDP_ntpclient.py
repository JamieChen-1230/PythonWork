from socket import *

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('>>> ').strip()
    udp_client.sendto(msg.encode('utf-8'), ip_port)  # UDP無鏈結，只能send時決定發給誰
    data, addr = udp_client.recvfrom(buffer_size)
    print('服務端標準時間為 ', data.decode('utf-8'))