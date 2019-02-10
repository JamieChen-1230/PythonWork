# ---------------------採集數據---------------------
# 不能用os實現，因為os不會返回數據
import subprocess
import requests

result = subprocess.getoutput("ipconfig")
# print(result)

# 透過正則獲取想要的數據，並整理
data_dict = {
    "network": {},
    "IPv4": {},
}

# ---------------------發送數據---------------------
requests.post("http://127.0.0.1:8000/assets.html", data=data_dict)
