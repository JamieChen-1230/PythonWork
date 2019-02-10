# 日誌功能
import logging
# 日誌級別
# logging.debug("debug message")
# logging.info("info message")
# # 因為默認是warning級別，所以只有warning以上的級別會顯示
# logging.warning("warning message")  # => WARNING:root:warning message
# logging.error("error message")  # => ERROR:root:error message
# logging.critical("critical message")  # => CRITICAL:root:critical message

# --------basicConfig--------(少用)
# # 改變參數
# logging.basicConfig(
#     level=logging.DEBUG,  # 把級別設為debug級別，所以會顯示debug以上的級別
#     filename="logger.log",  # 默認是顯示於螢幕，此為把信息添加到logger.log
#     filemode="w",  # 默認是"a"
#     format="%(asctime)s %(filename)s %(levelname)s [%(lineno)d] (%(message)s)"   # 更改格式
# )
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

# --------logger--------
# logger = logging.getLogger()
#
# fh = logging.FileHandler("logger.log")  # 向文件發布內容
# ch = logging.StreamHandler()  # 向螢幕打印內容
#
# m = logging.Formatter("%(asctime)s %(filename)s %(levelname)s [%(lineno)d] (%(message)s)")
# fh.setFormatter(m)  # fh加入格式
# ch.setFormatter(m)  # ch加入格式
#
# logger.addHandler(fh)  # logger加入向文件發布內容功能(fh)
# logger.addHandler(ch)  # logger加入向螢幕打印內容功能(ch)
# logger.setLevel("DEBUG")   # 設為debug級別
#
# logger.debug("debug message")  # => 2018-07-21 17:39:31,905 logging模塊.py DEBUG [39] (debug message)
# logger.info("info message")  # => 2018-07-21 17:39:31,905 logging模塊.py INFO [40] (info message)
# logger.warning("warning message")  # => 2018-07-21 17:39:31,905 logging模塊.py WARNING [41] (warning message)
# logger.error("error message")  # => 2018-07-21 17:39:31,906 logging模塊.py ERROR [42] (error message)
# logger.critical("critical message")  # => 2018-07-21 17:39:31,906 logging模塊.py CRITICAL [43] (critical message)

# --------logger+函數--------
# def logger():
#     logger = logging.getLogger()
#
#     fh = logging.FileHandler("logger.log")  # 向文件發布內容
#     ch = logging.StreamHandler()  # 向螢幕打印內容
#
#     m = logging.Formatter("%(asctime)s %(filename)s %(levelname)s [%(lineno)d] (%(message)s)")
#     fh.setFormatter(m)  # fh加入格式
#     ch.setFormatter(m)  # ch加入格式
#
#     logger.addHandler(fh)  # logger加入向文件發布內容功能(fh)
#     logger.addHandler(ch)  # logger加入向螢幕打印內容功能(ch)
#     logger.setLevel("DEBUG")   # 設為debug級別
#     return logger
#
# logger = logger()
# logger.debug("debug message")  # => 2018-07-21 17:39:31,905 logging模塊.py DEBUG [39] (debug message)
# logger.info("info message")  # => 2018-07-21 17:39:31,905 logging模塊.py INFO [40] (info message)
# logger.warning("warning message")  # => 2018-07-21 17:39:31,905 logging模塊.py WARNING [41] (warning message)
# logger.error("error message")  # => 2018-07-21 17:39:31,906 logging模塊.py ERROR [42] (error message)
# logger.critical("critical message")  # => 2018-07-21 17:39:31,906 logging模塊.py CRITICAL [43] (critical message)

# 子用戶不可重複
# logger1 = logging.getLogger("jamie")  # jamie為子用戶
# logger1.setLevel("DEBUG")  # 為debug級別
# logger1
#
# logger2 = logging.getLogger("jamie")  # jamie為子用戶
# logger2.setLevel("INFO")  # 為info級別
#
# fh = logging.FileHandler("logger.log")  # 向文件發布內容
# ch = logging.StreamHandler()  # 向螢幕打印內容
#
# logger1.addHandler(fh)
# logger1.addHandler(ch)
#
# logger2.addHandler(fh)
# logger2.addHandler(ch)
#
# logger1.debug("debug message")
# logger1.info("info message")
# logger1.warning("warning message")
# logger1.error("error message")
# logger1.critical("critical message")
#
# logger2.debug("debug message")
# logger2.info("info message")
# logger2.warning("warning message")
# logger2.error("error message")
# logger2.critical("critical message")
# # =>
# # info message
# # warning message
# # error message
# # critical message
# # info message
# # warning message
# # error message
# # critical message
# # logger1的debug沒有被打印，原因是子用戶都是唯一的
# # 同一個用戶只能有一種規範
# # 所以logger2覆蓋掉logger1
