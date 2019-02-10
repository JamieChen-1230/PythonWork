# 摘要算法，只能把明文轉密文(加密)
import hashlib

# md5
# # 因網路上有數據庫所以還是可以輕易被解
# # obj = hashlib.md5()
# # obj.update("hello".encode("utf8"))
# # print(obj.hexdigest())  # => 5d41402abc4b2a76b9719d911017c592，轉出來的密文跟明文是唯一的對應關係
#
# obj = hashlib.md5("sb".encode("utf8"))  # 在md5的基礎上加上固定的其他字符，增加難度
# obj.update("hello".encode("utf8"))
# print(obj.hexdigest())  # => 9a4f710207fb80475eae6bf9d61751e2，這個密文就想當sbhello轉換過來的密文
