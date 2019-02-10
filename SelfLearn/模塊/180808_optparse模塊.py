import optparse
# 用來替代sys.argv

# 創建一個OptionParser
parser = optparse.OptionParser()

# 新建選項
# add_option() 前面的是參數選項，一般就是前面短名後面長名
# dest：可以決定後來取值時的名字，默認是選項不加--的字符串。
# type：限制類別，默認選項為字符串
parser.add_option("-s", "--server", dest="Server", type=int)  # 可以用-s或--server調用
parser.add_option("-P", "--port")

options, args = parser.parse_args()  # 返回cmd中之輸入值
print(options)  # cmd中輸入上述有定義的格式資料會放進options，輸出為一個對象
print(options.Server)
print(args)  # 而剩下無定義的則放入args，輸出為一個list
print(args[0])
