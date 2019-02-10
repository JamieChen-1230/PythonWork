import subprocess

res = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE)  # 將內容裝進pipe(管道)裡
print(res)  # => <subprocess.Popen object at 0x000001B90E4B79B0>
# print(res.stdout.read())  # 讀出管道內的內容
print(res.stdout.read().decode('BIG5'))