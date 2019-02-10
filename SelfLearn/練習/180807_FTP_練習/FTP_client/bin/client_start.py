import os, sys

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024

if __name__ == "__main__":
    # print(os.path.abspath(__file__))  # __file__='start.py'
    # print(os.path.dirname(os.path.abspath(__file__)))  # D:\PythonWork\SelfLearn\練習\FTP\FTP_client\bin
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # D:\PythonWork\SelfLearn\練習\FTP\FTP_client
    FTP_client_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(FTP_client_path)
    # print(sys.path)
    from src import client
    data = sys.argv
    client.conn(ip_port, buffer_size, data[1], data[2])

