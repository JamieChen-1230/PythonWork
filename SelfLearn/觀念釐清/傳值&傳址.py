"""
Python傳參一律是傳『對象引用』，而Python內的數據分為可變與不可變，
當為不可變對象之引用，就相當於為傳值(不能修改原始對象值)，EX：數字、字符串、元組
當為可變對象之引用，就相當於為傳址(會修改原始對象值)，EX：列表、字典
"""
int_ = 1
float_ = 1.0
str_ = "jamie"
bool_ = True
dict_ = {"name": "jamie"}
list_ = [1]


def t(int_, float_, str_, bool_, dict_, list_):
    int_ = 100
    float_ = 100.0
    str_ = str_.replace("jamie", "100")
    bool_ = False
    dict_.setdefault("age", 22)
    list_.append(100)


t(int_, float_, str_, bool_, dict_, list_)
print(int_, float_, str_, bool_, dict_, list_)
