import socket, optparse, json, os

STATUS_CODE = {
    253: "帳號密碼錯誤",
    254: "登入成功"
}
class ClientHandler:

    def __init__(self):
        self.parser = optparse.OptionParser()
        self.parser.add_option("-s", "--server", dest="server")
        self.parser.add_option("-P", "--port", dest="port")
        self.parser.add_option("-u", "--username", dest="username")
        self.parser.add_option("-p", "--password", dest="password")

        self.options, self.args = self.parser.parse_args()
        self.verify_args()
        self.make_conn()
        self.mainpath = os.path.dirname(os.path.abspath(__file__))

    # def response(self):
    #     data = self.sock.recv(1024).decode('utf-8')
    #     data = json.loads(data)
    #     return data

    def verify_args(self):
        port = self.options.port
        if int(port)>0 and int(port)<65535:
            return True
        else:
            exit('the port is in 0-65535')

    def make_conn(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.options.server, int(self.options.port)))

    def interactive(self):
        if self.authenticate():
            print('-----start to interactive-----')
            while True:
                cmd_info = input("[%s] " % self.current_dir).strip()
                cmd_list = cmd_info.split()
                if cmd_list[0] == 'exit':
                    break
                if hasattr(self, cmd_list[0]):
                    func = getattr(self, cmd_list[0])
                    func(*cmd_list)

    def put(self, *cmd_list):
        # (0)put (1)文件名 (2)額外目錄(默認放在家目錄下)
        action, local_path, target_path = cmd_list
        local_path = os.path.join(self.mainpath, local_path)

        file_name = os.path.basename(local_path)  # 文件名
        file_size = os.stat(local_path).st_size

        data = {
            'action': 'put',
            'file_name': file_name,
            "file_size": file_size,
            'target_path': target_path
        }

        self.sock.send(json.dumps(data).encode('utf-8'))

        is_exist = self.sock.recv(1024).decode('utf-8')  # 回傳文件是否存在
        print(is_exist)
        has_sent = 0
        if is_exist == "800":
            # 文件不完整
            choice = input("檔案已存在但不完整，是否續傳(y/n) ").strip()
            if choice.upper() == "Y":
                self.sock.send("Y".encode('utf-8'))
                has_sent = int(self.sock.recv(1024).decode('utf-8'))
            else:
                self.sock.send("N".encode('utf-8'))
        elif is_exist == "801":
            # 文件完整存在
            print('檔案已存在')
            return
        # 802 文件不存在，直接傳

        f = open(local_path, 'rb')
        f.seek(has_sent)  # 從還未傳的部份開始傳

        while has_sent < file_size:
            data = f.read(1024)
            self.sock.sendall(data)
            has_sent += len(data)
            self.progress_bar(has_sent, file_size)
        f.close()
        print('上傳成功!')

    def progress_bar(self, has, total):
        rate = float(has)/float(total)
        percent = int(rate*100)
        # /r 表示將光標的位置回退到本行的開頭位置，這樣就能顯示在同意行了
        print('%s%% %s\r' % (percent, '*'*percent), end='')

    def authenticate(self):
        if self.options.username is None and self.options.password is None:
            username = input("username: ")
            password = input("password: ")
            return self.get_auth_result(username, password)
        return self.get_auth_result(self.options.username, self.options.password)

    def get_auth_result(self, username, password):
        data = {
            'action': 'auth',
            "username": username,
            "pwd": password
        }
        self.sock.send(json.dumps(data).encode('utf-8'))
        data = self.sock.recv(1024).decode('utf-8')
        data = json.loads(data)
        print("state_code: ", data["state_code"])
        if data["state_code"] == 254:
            self.user = username
            self.current_dir = username
            print(STATUS_CODE[254])
            return True  # 用於interactive()
        else:
            print(STATUS_CODE[data["state_code"]])

    def ls(self, *cmd_list):
        data = {
            'action': 'ls'
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        data = self.sock.recv(1024).decode('utf-8')
        print(data)

    def cd(self, *cmd_list):
        # cd images
        data = {
            'action': 'cd',
            'dirname': cmd_list[1]
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        cd_path = self.sock.recv(1024).decode('utf-8')
        # print(cd_path)
        if cd_path != '無此資料夾':
            self.current_dir = os.path.basename(cd_path)
        else:
            print('無此資料夾')

    def mkdir(self, *cmd_list):
        data = {
            'action': 'mkdir',
            'dirname': cmd_list[1]
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        res = self.sock.recv(1024).decode('utf-8')
        print(res)

    def rmdir(self, *cmd_list):
        data = {
            'action': 'rmdir',
            'dirname': cmd_list[1]
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        data = self.sock.recv(1024).decode('utf-8')
        print(data)

ch1 = ClientHandler()
ch1.interactive()
