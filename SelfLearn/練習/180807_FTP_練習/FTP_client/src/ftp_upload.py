import pickle, os, struct
from conf import setting

def upload(filename):
    f_name = setting.db_path + os.sep + filename
    with open(f_name, 'r') as f:
        data = f.read()
    data_dic = {
        'filename': filename,
        'data': data
    }
    pickle_data = pickle.dumps(data_dic)  # 經pickle轉換後的檔案字典
    l_pickle_data = len(pickle_data)
    pack_pickle_data = struct.pack('i', l_pickle_data)

    return pack_pickle_data, pickle_data
