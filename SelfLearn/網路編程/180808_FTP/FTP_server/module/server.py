# 服務端程序
import socketserver, json, os
import configparser
from conf import settings

STATUS_CODE = {
    253: "帳號密碼錯誤",
    254: "登入成功",

    800: "文件存在，但不完整，請傳送數據",
    801: "文件已完整存在",
    802: "準備接收數據"
}

class ServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            # conn = self.request
            data = self.request.recv(1024).strip()
            if not data: break
            data = json.loads(data.decode('utf-8'))
            '''{
                'action': ,
                'username': ,
                'pwd': 
            }
            '''
            if data.get("action"):
                if hasattr(self, data.get("action")):
                    func = getattr(self, data.get("action"))
                    func(**data)
                else:
                    print('無效指令1')
            else:
                print('無效指令2')

    def send_response(self, state_code):
        response = {
            "state_code": state_code
        }
        self.request.send(json.dumps(response).encode('utf-8'))

    def auth(self, **data):  # 認證
        username = data['username']
        password = data['pwd']

        user = self.authenticate(username, password)
        if user:
            self.send_response(254)
        else:
            self.send_response(253)

    def authenticate(self, username, password):
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_PATH)

        if username in config.sections():
            if config[username]["Password"] == password:
                print('登入成功')
                self.user = username
                self.mainpath = os.path.join(settings.BASE_DIR, 'home', self.user)
                return username

    def put(self, **data):  # 認證
        print("data", data)
        file_name = data.get("file_name")
        file_size = data.get('file_size')
        target_path = data.get('target_path')
        if not target_path:
            file_path = os.path.join((self.mainpath, file_name))
        else:
            file_path = os.path.join(self.mainpath, target_path, file_name)

        has_recv_size = 0
        if os.path.exists(file_path):
            # 文件已存在
            has_file_size = os.stat(file_path).st_size
            if has_file_size < file_size:
                # 斷點續傳
                self.request.sendall("800".encode('utf-8'))
                choice = self.request.recv(1024).decode('utf-8')
                if choice == "Y":
                    # 續傳
                    self.request.sendall(str(has_file_size).encode('utf-8'))
                    has_recv_size = has_file_size
                    f = open(file_path, 'ab')  # 要用'ab'模式
                else:
                    # 不續傳 = 重傳
                    f = open(file_path, 'wb')
            else:
                # 文件已完整存在
                self.request.sendall("801".encode('utf-8'))
                return
        else:
            # 文件不存在
            self.request.sendall("802".encode('utf-8'))
            f = open(file_path, 'wb')

        while has_recv_size < file_size:
            try:
                data = self.request.recv(1024)
            except Exception:
                break
            f.write(data)
            has_recv_size += len(data)

        f.close()

    def ls(self, **data):

        file_list = os.listdir(self.mainpath)  # list
        if not len(file_list):
            data = "資料夾內無檔案"
        else:
            data = "\n".join(file_list)  # str
        self.request.sendall(data.encode('utf-8'))

    def cd(self, **data):
        dirname = data.get('dirname')
        if dirname == '..':
            self.mainpath = os.path.dirname(self.mainpath)
            self.request.sendall(self.mainpath.encode('utf-8'))
        elif os.path.exists(os.path.join(self.mainpath, dirname)):
            self.mainpath = os.path.join(self.mainpath, dirname)
            self.request.sendall(self.mainpath.encode('utf-8'))
        else:
            self.request.sendall('無此資料夾'.encode('utf-8'))

    def mkdir(self, **data):
        dirname = data.get('dirname')
        path = os.path.join(self.mainpath, dirname)
        if not os.path.exists(path):
            if "/" in dirname:
                os.makedirs(path)  # 創建多個資料夾
            else:
                os.mkdir(path)  # 創建單個資料夾
            self.request.sendall('創建成功'.encode('utf-8'))
        else:
            self.request.sendall('資料夾已存在'.encode('utf-8'))

    def rmdir(self, **data):
        dirname = data.get('dirname')
        if os.path.exists(os.path.join(self.mainpath, dirname)):
            os.rmdir(os.path.join(self.mainpath, dirname))
            self.request.sendall('刪除成功'.encode('utf-8'))
        else:
            self.request.sendall('無此資料夾'.encode('utf-8'))







