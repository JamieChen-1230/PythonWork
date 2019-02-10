# ---------random模塊---------
import random
# random.random() (0, 1)之間的浮點數
# res = random.random()
# print(res)  # => 0.13268427262417348，0到1的浮點數

# random.uniform() 浮點數亂數
# print(random.uniform(1, 3))  # => 2.221417950051589

# random.randint() 整數亂數
# print(random.randint(1, 3))  # 1到3隨機
# print(random.randrange(1, 3))  # 1到2隨機

# random.choice() 隨機選取可跌代對象元素
# print(random.choice("ABC"))
# print(random.sample([11, 22, 33], 2))  # 可選取多個元素

# random.shuffle() 重組順序
# item = [1, 2, 3, 4]
# random.shuffle(item)
# print(item)  # => [3, 2, 1, 4]
