import os, sys

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024

if __name__ == "__main__":
    FTP_server_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(FTP_server_path)
    # print(sys.path)
    from src import server
    server.conn(ip_port, buffer_size)
