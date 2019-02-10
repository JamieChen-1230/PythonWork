from bs4 import BeautifulSoup

# 更多於https://www.cnblogs.com/wupeiqi/articles/6283017.html

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
    <p>self</p>
    <div id="outer" name="outer">
        <p>outer1</p>
        <div id="inner">
            <p id="inner">inner</p>
        </div>
        <p>outer2</p>
    </div>
    <p>self2</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, features="lxml")

"""tag.name 返回是哪種標籤"""
# tag = soup.find(id="outer")
# print(tag.name)  # => div

"""tag.string 返回該標籤的文本"""
# tag = soup.find(id="outer")
# print(tag.string)  # => None

"""tag.attrs 返回標籤所有屬性"""
# tag = soup.find(id="outer")
# print("tag.attrs:", tag.attrs)  # => {'id': 'outer', 'name': 'outer'}
# tag.attrs = {"test": "test", "test2": "test2"}  # 重新賦予屬性
# del tag.attrs["test"]  # 刪除屬性
# print("tag.attrs:", tag.attrs)  # => {'test2': 'test2'}

"""tag.children 返回所有子標籤"""
# tag = soup.find(id="outer")
# print("tag.children:", tag.children)  # => <list_iterator object at 0x0000014E5EB60CC0>
# from bs4.element import Tag
# for t in tag.children:
#     if type(t) == Tag:  # 只找標籤對象
#         # print(type(t))
#         print(t)

"""tag.descendants 返回所有後代標籤"""
# tag = soup.find(id="outer")
# print("tag.children:", tag.descendants)  # => <generator object descendants at 0x0000022A3A940E08>
# from bs4.element import Tag
# for t in tag.descendants:
#     if type(t) == Tag:  # 只找標籤對象
#         # print(type(t))
#         print(t)

"""tag.clear() 將標籤的所有子標籤全部清空（保留標籤名）"""
# tag = soup.find(id="outer")
# tag.clear()
# print(tag)  # => <div id="outer" name="outer"></div>

"""tag.decompose() 遞歸的刪除所有的標籤（不保留標籤名）"""
# tag = soup.find(id="outer")
# tag.decompose()
# print(tag)  # => <None></None>

"""tag.decode() 轉換為字符串（含當前標籤）；decode_contents（不含當前標籤）"""
# tag = soup.find(id="outer")
# print(tag.decode())

"""tag.encode() 轉換為字節（含當前標籤）；encode_contents（不含當前標籤）"""
# tag = soup.find(id="outer")
# print(tag.encode())

"""find 獲取匹配的第一個標籤，參數有name,attrs,recursive,text"""
# tag = soup.find(name="div", attrs={"id": "outer"})
# print(tag)
# recursive=False 不遞規，只在子代裡找；text 文本要符合
# tag = soup.find(name="div", attrs={"id": "outer"}).find("p", recursive=False, text="outer")
# print(tag)  # => <p>outer</p>

"""find_all 獲取匹配的所有標籤，參數有name,attrs,recursive,text"""
# tag = soup.find_all(name=["div", "p"])  # 找所有的div或p標籤
# print(tag)
# tag = soup.find_all(id=["inner", "outer"])  # 找所有的id為inner或outer標籤
# print(tag)
# ----------正則----------
# import re
# rep = re.compile("o+")
# tag = soup.find_all(id=rep)  # 找所有id包含o的標籤
# print(tag)

"""tag.has_attr 檢查標籤是否具有該屬性"""
# tag = soup.find(name="div", attrs={"id": "outer"})
# print(tag.has_attr("id"))  # => True

"""tag.index 檢查標籤在某標籤中的索引位置"""
# tag = soup.find(name="body")
# v = tag.index(tag.find("div"))
# print(v)

"""關聯標籤"""
# tag = soup.find(id="inner")
# -------父親標籤-------
# print(tag.parent)
# -------父輩標籤-------
# print(list(tag.parents))
# -------後一個標籤-------
# print(list(tag.next_element))
# -------後面所有標籤-------
# print(list(tag.next_elements))
# -------前一個標籤-------
# print(list(tag.previous_element))
# -------前面所有標籤-------
# print(list(tag.previous_elements))
# -------兄弟標籤中，後一個標籤-------
# print(list(tag.next_sibling))
# -------兄弟標籤中，後面所有標籤-------
# print(list(tag.next_siblings))
# -------兄弟標籤中，前一個標籤-------
# print(list(tag.previous_sibling))
# -------兄弟標籤中，前面所有標籤-------
# print(list(tag.previous_siblings))

"""關聯標籤中的某標籤"""
# tag = soup.find(id="inner")
# -------找到祖輩且為div的標籤-------
# print(tag.find_parent("div"))
# -------找到所有祖輩且為div的標籤-------
# print(tag.find_parents("div"))
# -------找到所有在後面且為p的標籤-------
# print(tag.find_all_next("p"))
# -------兄弟標籤中，找到在後一個且為p的標籤-------
# print(tag.find_next_sibling("p"))
# -------兄弟標籤中，找到所有在後面且為p的標籤-------
# print(tag.find_next_siblings("p"))
# -------找到所有在前面且為p的標籤-------
# print(tag.find_all_previous("p"))
# -------兄弟標籤中，找到在前一個且為p的標籤-------
# print(tag.find_previous_sibling("p"))
# -------兄弟標籤中，找到所有在前面且為p的標籤-------
# print(tag.find_previous_siblings("p"))

"""類似CSS選擇器"""
# -------所有body標籤子代中的p標籤-------
# print(soup.select("body > p"))
# -------所有body標籤後代中的p標籤-------
# print(soup.select("body p"))
# -------所有title和p標籤-------
# print(soup.select("title,p"))
# -------所有id為inner的div-------
# print(soup.select("div[id='inner']"))
# -------所有id為inner的標籤-------
# print(soup.select("#inner"))
