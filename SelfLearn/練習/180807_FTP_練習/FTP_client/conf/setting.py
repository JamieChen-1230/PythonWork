import os, sys

# print(os.path.abspath(__file__))  # __file__='start.py'
# print(os.path.dirname(os.path.abspath(__file__)))  # D:\PythonWork\SelfLearn\練習\FTP\FTP_client\bin
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # D:\PythonWork\SelfLearn\練習\FTP\FTP_client
FTP_client_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(FTP_client_path)
db_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'db'
# print(db_path)
conf_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'conf'
# print(conf_path)
