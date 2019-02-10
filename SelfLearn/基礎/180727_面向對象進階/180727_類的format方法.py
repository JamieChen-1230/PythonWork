# class Date:
#     def __init__(self, y, m ,d):
#         self.year = y
#         self.month = m
#         self.day = d
#
# d1 = Date(2016, 12, 26)
#
# x = "{0} {0} {0}".format(d1)
# print(x)
# # => <__main__.Date object at 0x000001F5130E9278> <__main__.Date object at 0x000001F5130E9278> <__main__.Date object at 0x000001F5130E9278>
#
# y = "{0.year} {0.month} {0.day}".format(d1)
# print(y)  # => 2016 12 26


# __format__
class Date:
    def __init__(self, y, m ,d):
        self.year = y
        self.month = m
        self.day = d

    def __format__(self, format_spec):
        print("執行__format__")
        return "{0.year}{1}{0.month}{1}{0.day}".format(self, format_spec)  # format_spec預設為空白

d1 = Date(2016, 12, 26)
print(format(d1, '-'))  # => 2016-12-26
