import pandas as pd
import numpy as np


# --------------------Pandas資料結構--------------------
# Series欄位(一維度)
"""
Series欄位：
多用來處理時間序列相關的資料，例如感測器資料，
利用pd.Series(串列or字典or單一資料, index)即可創建一個series，
index不輸入預設為0, 1, 2....
"""
# 串列
# s1 = pd.Series(["a", "b", "c"])
# print(s1)
# print("================")
# s2 = pd.Series(["a", "b", "c"], index=["i1", "i2", "i3"])  # list數和index數須相等
# print(s2)
# print("================")
# print(s2[0])  # 依然可透過索引找

# 字典
# dic = {"name": "jamie", "age": 22, "date": "85.12.30"}
# s = pd.Series(dic, index=dic.keys())
# print(s)
# print("================")
# print(s["name"])
# print("================")
# print(s[:2])

# 單一資料
# data = "Jamie"
# s = pd.Series(data)
# print(s)
# print("================")
# s1 = pd.Series(data, index=range(3))
# print(s1)


# DataFrame表格(二維度)
"""
DataFrame表格：
多用來處理結構化資料，有列索引與欄標籤的二維資料集，例如關聯式資料庫、CSV
"""
# 串列
# li = [["Movies", 46], ["Sports", 8], ["Coding", 12], ["Fishing", 12], ["Dancing", 6], ["cooking", 8]]
# d = pd.DataFrame(li)
# print(d)
# print("================")
# d = pd.DataFrame(li, columns=["name", "num"])  # 指定欄位名
# print(d)

# 字典
# groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]
# num = [46, 8, 12, 12, 6, 58]
# dic = {"groups": groups, "num": num}
# d = pd.DataFrame(dic)  # 欄位名為keys
# print(d)

# 隨機值
# groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]
# d = pd.DataFrame(np.random.rand(4, 6), columns=groups)
# print(d)

# --------------------DataFrame基礎方法--------------------
groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]
num = [46, 8, 12, 12, 6, 58]
dic = {"groups": groups, "num": num}
d = pd.DataFrame(dic)  # 欄位名為keys

# shape 回傳列數與欄數
# print(d.shape)  # => (6, 2)

# describe() 回傳描述性統計(平均值、最大值、總數等)
# print(d.describe())

# head() 回傳前幾筆
# print(d.head(3))  # 前三筆

# tail() 回傳後幾筆
# print(d.tail(3))  # 後三筆

# columns 回傳欄位名
# print(d.columns)  # => Index(['groups', 'num'], dtype='object')

# values 回傳內容值
# print(d.values)

# index 回傳index
# print(d.index)  # => RangeIndex(start=0, stop=6, step=1)

# info 回傳資料內容
# print(d.info)

# .T 轉置
# print(d.T)


# --------------------DataFrame選擇與篩選--------------------
groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]
num = [46, 8, 12, 12, 6, 58]
dic = {"groups": groups, "num": num}
d = pd.DataFrame(dic)

# 中括號 [] 選擇元素
# print(d["groups"])
# print("================")
# print(d["groups"][3])

# .loc 通過行列標籤值取值，[列, 行]
# print(d.loc[:])  # 全取
# print("================")
# print(d.loc[0:3])  # 取0-3列
# print("================")
# print(d.loc[:, "groups"])  # 取groups欄的全部值，等同於d.iloc[:, 0]

# .iloc 通過行列數字索引取值，[列, 行]
# print(d.iloc[0, 1])  # 第一列第二欄：組的人數
# print("================")
# print(d.iloc[0:1, :])  # 第一列：組的組名與人數
# print("================")
# print(d.iloc[:, 1])  # 第二欄：各組的人數
# print("================")
# print(d.iloc[2])  # 第三列

# .ix 結合loc和iloc
# print(d.ix[0:3, 0])  # (0-3, 0)
# print("================")
# print(d.ix[0:3, "groups"])  # (0-3, 0)
# print("================")
# print(d.ix[0:3, :])  # (0-3, all)

# 進階篩選(布林值取法)
# print(d.iloc[:, 1] > 10)  # 產生 T or F
# print("================")
# print(d[d.iloc[:, 1] > 10])  # 根據 T or F，選出人數超過 10 的群組


# --------------------DataFrame選擇與篩選--------------------
groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]
num = [46, 8, 12, 12, 6, 58]
dic = {"groups": groups, "num": num}
d = pd.DataFrame(dic)

# .sort_index() 根據索引值排序
# axis=0依據index排序；axis=1依據columns排序
# ascending 用於設定升冪或降密
# print(d.sort_index(axis=0, ascending=False))

# .sort_values() 根據欄位排序
# print(d.sort_values(by='num'))  # 透過num的數值排序
# print("================")
# print(d.sort_values(by='groups'))  # 透過groups的數值排序


# --------------------DataFrame處理遺漏值--------------------
# 讀取csv並產生DataFrame
df = pd.read_csv("shop_list2.csv")
select_df = pd.DataFrame(df)

# isnull() 是否為空
# print(select_df.ix[:, "shop name"].isnull())  # 判斷哪些店名是遺失值

# notnull() 是否不為空
# print(select_df.ix[:, "shop name"].notnull())  # 判斷哪些店名不是遺失值

# dropna() 刪除為空的列
# drop_df = select_df.dropna()
# print(select_df)
# print("================")
# print(drop_df)

# fillna() 自動填補
# fill_df = select_df.fillna(87)
# print(select_df)
# print("================")
# print(fill_df)


# --------------------DataFrame資料操作--------------------
# 合併資料
# left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
# right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
# print(pd.merge(left, right, on='key'))

# 新增資料
# df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
# print(df)
# print("================")
# s = df.iloc[3]
# print(s)
# print("================")
# print(df.append(s, ignore_index=True))  # 添加到最後

# 分組
# col = ['class', 'name', 'hbd']
# data = [['class0', 'user0', '1993-10-01'],
#         ['class0', 'user1', '1992-10-02'],
#         ['class1', 'user2', '1990-10-01'],
#         ['class2', 'user3', '1983-10-03'],
#         ['class1', 'user4', '1991-10-02'],
#         ['class0', 'user5', '2001-10-03']]
# df = pd.DataFrame(data, columns=col)
# print(df.groupby("class"))  # => <pandas.core.groupby.DataFrameGroupBy object at 0x0000025E8717C470>
# print(df.groupby("class").groups)  # 顯示分組過後分別包含哪幾項的索引
# print(df.groupby("class").get_group("class0"))  # 顯示有關class0的資料


# 分組
# df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
#                    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
#                    'C': np.random.randn(8),
#                    'D': np.random.randn(8)})
# print(df.groupby("A").sum())  # 計算A中兩群組總和
