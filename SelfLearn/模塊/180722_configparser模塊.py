# 讀取配置文件
import configparser
config = configparser.ConfigParser()  # config{}

# 不同的寫入方式
# config["DEFAULT"] = {"ServerAliveInterval" : "45",
#                      "Compression": "yes",
#                      "CompressionLevel": "9"}
# config["User"] = {}
# config["User"]["Name"] = "jamie"
#
#
# with open("config.ini", "w") as f:
#     config.write(f)  # config的寫入方式

# 查詢
# config.read("config.ini")
# print(config.sections())  # => ['User']，除了DEFAULT之外的取出
# print('User' in config)  # => True
# print(config["User"]["Name"])  # => jamie

# for i in config["User"]:
#     print(i)
# =>
# name  # User底下的資訊
# compression  # DEFAULT底下的資訊，不管循環哪個區塊，都會顯示DEFAULT的資料
# serveraliveinterval
# compressionlevel

# print(config.options("User"))  # => ['name', 'compression', 'serveraliveinterval', 'compressionlevel']，取鍵
# print(config.items("User"))
# # => [('compression', 'yes'), ('serveraliveinterval', '45'), ('compressionlevel', '9'), ('name', 'jamie')]，取鍵加值

# 修改
# config.read("config.ini")
# config.add_section("Age")
# config.set("Age", "SB", "20")
# config.set("Age", "NB", "87")
#
# with open("config.ini", "w") as f:
#     config.write(f)

# 刪除
# config.read("config.ini")
# # config.remove_option("Age", "NB")  # 刪單獨值
# config.remove_section("Age")  # 全刪
#
# with open("config.ini", "w") as f:
#     config.write(f)
