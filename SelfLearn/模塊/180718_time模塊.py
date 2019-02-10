# 模塊讀取順序是照sys.path的路徑順序找的，所以創建與內置模塊相同名稱的文件時會覆蓋掉內置文件
# ---------time模塊---------
import time
# time.time() 時間戳(做計算用 end - start)
# print(time.time())  # => 1531887232.683761(秒)，從1970年(unix誕生日期)到現在所經過的秒數

# 結構化時間(由時間戳轉換而來)
# time.localtime() 當地的時間，默認參數為時間戳時間(time.time())
# t = time.localtime()
# print(t)
# # => time.struct_time(tm_year=2018, tm_mon=7, tm_mday=18, tm_hour=12, tm_min=21, tm_sec=44, tm_wday=2, tm_yday=199)
# print(t.tm_year)  # => 2018
# time.gmtime() 英國格林威治時間，默認參數為時間戳時間(time.time())
# print(time.gmtime())
# # => time.struct_time(tm_year=2018, tm_mon=7, tm_mday=18, tm_hour=4, tm_min=23, tm_sec=17, tm_wday=2, tm_yday=199)

# time.mktime() 將結構化時間轉為時間戳
# print(time.mktime(time.localtime()))  # => 1531888405
# print(time.time())  # => 1531888405.4044104

# time.strftime() 將結構化時間轉為自定義字符串時間(%Y年, %m月, %d日, %X時分秒)
# print(time.strftime("%Y--%m--%d %X", time.localtime()))  # => 2018--07--18 12:39:40

# time.strptime() 將自定義字符串時間轉為結構化時間(前後要一一對應)
# print(time.strptime("2016:12:24:17:50:36", "%Y:%m:%d:%X"))
# # => time.struct_time(tm_year=2016, tm_mon=12, tm_mday=24, tm_hour=17, tm_min=50, tm_sec=36, tm_wday=5, tm_yday=359, tm_isdst=-1)

# time.asctime() 固定的字符串時間
# print(time.asctime())  # => Wed Jul 18 12:46:04 2018
# print(time.ctime())  # => Wed Jul 18 12:46:04 2018

# time.sleep()延遲
# time.sleep(5)  # 參數單位為秒

# datetime(字符串形式)
# import datetime
# print(datetime.datetime.now())  # => 2018-07-18 12:52:24.630243
