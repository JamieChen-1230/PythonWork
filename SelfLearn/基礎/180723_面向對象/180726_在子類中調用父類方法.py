# 方法一 (較差)
# class Vehicle:
#     Country = "China"
#     def __init__(self, name, speed, load):
#         self.name = name
#         self.speed = speed
#         self.load = load
#
#     def run(self):
#         print("開動拉")
#
# class Subway(Vehicle):
#     def __init__(self, name, speed, load, num):
#         Vehicle.__init__(self, name, speed, load)  # 調用父類的init方法
#         self.num = num
#
#     def info(self):
#         print(self.name, self.num)
#
#     def run(self):
#         Vehicle.run(self)  # 調用父類的run方法
#         print("subway開動拉")
# subway1 = Subway("台鐵", "10km/hr", 10000, 13)
# subway1.info()
# subway1.run()


# 方法二 super (較好)
class Vehicle:
    Country = "China"
    def __init__(self, name, speed, load):
        self.name = name
        self.speed = speed
        self.load = load

    def run(self):
        print("開動拉")

class Subway(Vehicle):
    def __init__(self, name, speed, load, num):
        # Vehicle.__init__(self, name, speed, load)  # 調用父類的init方法
        super().__init__(name, speed, load)  # 調用父類的init方法，不用加self
        self.num = num

    def info(self):
        print(self.name, self.num)

    def run(self):
        # Vehicle.run(self)  # 調用父類的run方法
        super().run()  # 調用父類的run方法，不用加self
        print("subway開動拉")
subway1 = Subway("台鐵", "10km/hr", 10000, 13)
subway1.info()
subway1.run()
print(subway1.__class__)