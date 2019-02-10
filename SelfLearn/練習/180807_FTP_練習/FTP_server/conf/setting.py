import os, sys

FTP_server_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(FTP_server_path)
db_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'db'
# print(db_path)
conf_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'conf'
# print(conf_path)