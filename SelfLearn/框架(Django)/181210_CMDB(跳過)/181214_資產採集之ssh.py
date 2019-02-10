# 基於paramiko, pip3 install paramiko
import requests
import paramiko

# ---------------------獲取今日未採集之主機名---------------------
# com_list = requests.get("http://127.0.0.1:8000/assets.html")
com_list = ["c1.com", "c2.com"]

# ---------------------通過paramiko連接遠程服務器, 執行命令---------------------
# 創建ssh對象
ssh = paramiko.SSHClient()
# 允許連接不存在know_hosts文件中的主機
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 連接服務器
ssh.connect(hostname="", port=22, username="", password="")

# 執行命令
stdin, stdout, stderr = ssh.exec_command("ipconfig")
# 獲取命令結果
result = stdout.read()

# 關閉連接
ssh.close()

# 透過正則獲取想要的數據，並整理
data_dict = {
    "network": {},
    "IPv4": {},
}

# ---------------------發送數據---------------------
requests.post("http://127.0.0.1:8000/assets.html", data=data_dict)
