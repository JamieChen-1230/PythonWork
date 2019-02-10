# ---------xml模塊---------(理解就好)
# 跟json一樣用來數據交換，是json出現前唯一的交換方式
import xml.etree.ElementTree as ET
tree = ET.parse("test_xml")  # => 解析xml檔，此為一個對象被放在tree變量
root = tree.getroot()  # 拿到根節點
# print(root.tag)  # => data，root標籤名

# 遍歷xml文件
# for i in root:  # 對data節點進行遍歷
#     # print(i, i.tag)  # 值為data的子節點的對象與標籤
#     # print(i.attrib)  # 值為data的子節點的屬性
#     for j in i:  # 對i節點進行遍歷
#         # print(j, j.tag)  # 值為i的子節點的對象與標籤
#         # print(j.attrib)  # 值為i的子節點的屬性
#         print(j.text)  # 值為i的子節點的文字內容

# 只遍歷year標籤(從外往裡找)
# for i in root.iter("year"):
#     print(i.tag, i.text)

# 修改
# for node in root.iter("year"):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)  # 修改內容
#     node.set("updated", "yes")  # 修改屬性
# tree.write("test_xml")  # 把修改的值寫入相同文件(也可寫入不同文件)

# 刪除
# for country in root.findall("country"):
#     rank = int(country.find("rank").text)
#     if rank < 5:
#         root.remove(country)  # 刪除
# tree.write("test_xml2.xml")

# 創建xml數據
# new_xml = ET.Element("namelist")  # => 創建<namelist><\namelist>
# name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})  # 在namelist中加入子標籤
# age = ET.SubElement(name, "age")  # 在name中加入子標籤
# age.text = '18'
#
# et = ET.ElementTree(new_xml)  # 生成文件檔對象
# et.write("new_xml.xml", encoding="utf-8", xml_declaration=True)  # 寫入
