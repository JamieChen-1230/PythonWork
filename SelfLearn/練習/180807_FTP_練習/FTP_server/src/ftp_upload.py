import os
from conf import setting

def upload(name, data):
    filename = setting.db_path + os.sep + name
    # print(filename)
    with open(filename, 'w') as f:
        f.write(data)
