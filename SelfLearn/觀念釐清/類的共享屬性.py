class Taiwanese:
    # 類屬性
    species = "people"
    country = "TW"

    def __init__(self, name, sex):
        # 實例屬性
        self.name = name
        self.sex = sex

    # 普通方法
    def walk(self):
        print("%s is walking" % self.name)

    # 靜態屬性
    @property
    def talk(self):
        print("%s is talking" % self.name)

    # 類方法
    @classmethod
    def born(cls):
        print("I born in %s" % cls.country)

    # 靜態方法
    @staticmethod
    def sum(x, y):
        print(x + y)


# 類屬性 => 共享、類與實例皆可調用
p1 = Taiwanese("Jamie", "男")
p2 = Taiwanese("Candy", "女")
Taiwanese.country = "CN"
print(p1.country, p2.country)
print(Taiwanese.country)

# 實例屬性 => 獨立、僅實例可調用
p1 = Taiwanese("Jamie", "男")
p2 = Taiwanese("Candy", "女")
p1.name = "Jamie2"
print(p1.name, p2.name)
# print(Taiwanese.name)  # => 報錯(AttributeError: type object 'Taiwanese' has no attribute 'name')

# 普通方法 => 共享、僅實例可調用
p1 = Taiwanese("Jamie", "男")
p2 = Taiwanese("Candy", "女")
def walk(self):
    print("%s is walking too" % self.name)
Taiwanese.walk = walk
p1.walk()
p2.walk()
# Taiwanese.walk()

# 靜態屬性 => 共享、僅實例可調用
p1 = Taiwanese("Jamie", "男")
p2 = Taiwanese("Candy", "女")
@property
def talk(self):
    print("%s is talking too" % self.name)
Taiwanese.talk = talk
p1.talk
p2.talk
# Taiwanese.talk

# 類方法 => 共享、類與實例皆可調用
p1 = Taiwanese("Jamie", "男")
p2 = Taiwanese("Candy", "女")
@classmethod
def born(cls):
    print("I born in %s too" % cls.country)
Taiwanese.born = born
p1.born()
p2.born()
Taiwanese.born()

# 靜態方法 => 共享、類與實例皆可調用
p1 = Taiwanese("Jamie", "男")
p2 = Taiwanese("Candy", "女")
@staticmethod
def sum(x, y):
    print(x + y + 1)
Taiwanese.sum = sum
p1.sum(1, 1)
p2.sum(1, 1)
Taiwanese.sum(1, 1)
