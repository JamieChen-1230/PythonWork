#  類 ：1.把一類事物的相同的特徵與動作整合到一起就是類。
#       2.類是一個抽象的概念
# 對象：1.就是基於類而創建的一個具體事物(具體存在的)
#       2.也是特徵和動作整合在一起

# 學校類：
# 特徵：name, addr, type
# 動作：考試, 招生

def school(name, addr, type):  # 不讓學校以外的事物使用
    def init(name, addr, type):
        school_data = {
            'name': name,
            'addr': addr,
            'type': type,
            'quiz': quiz,  # 把動作和特徵綁定
            'enroll': enroll
        }
        return school_data
    def quiz(school):
        print("%s 正在考試" % school['name'])
    def enroll(school):
        print("%s%s 正在招生" % (school['type'], school['name']))
    return init(name, addr, type)

s1 = school('台科', '台北', '私立')  # 創建對象
s1['quiz'](s1)