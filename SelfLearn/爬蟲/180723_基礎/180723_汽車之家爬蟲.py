import requests
from bs4 import BeautifulSoup

"""
response.encoding: 要以什麼編碼獲取網站資料
response.apparent_encoding: 返回網站本身的編碼
response.status_code: 返回網站目前的狀態
response.text: 返回資料數據類型為文本(str)
response.content: 返回資料數據類型為字節(bytes)

soup.find(): 找到第一個匹配的對象
soup.find_all(): 找出所有匹配的對象
obj.text: 返回標籤對象的文本
obj.attrs: 返回標籤對象的所有屬性
"""

"""1.下載頁面"""
response = requests.get(url='https://www.autohome.com.cn/news/')
# response.encoding 要以什麼編碼獲取網站資料；response.apparent_encoding 返回網站本身的編碼
response.encoding = response.apparent_encoding
# response.status_code 返回網站目前的狀態
print("status_code: ", response.status_code)

"""2.將html文本轉換為BeautifulSoup對象"""
# response.text 返回資料數據類型為文本
soup = BeautifulSoup(response.text, features="lxml")  # feature:處裡引擎，html.parser為python內建

"""3.過濾出想要資料"""
target = soup.find("div", id='auto-channel-lazyload-article')
# obj = target.find('li')  # find() 找到第一個匹配的BeautifulSoup對象
li_list = target.find_all('li')  # find_all() 找出所有匹配的BeautifulSoup對象，類型為list

for li in li_list:
    a = li.find('a')
    if a:  # 判斷是否有a標籤
        print("http:" + a.attrs.get("href"))  # a.attrs: a標籤的所有屬性，以字典形式呈現
        h3 = a.find('h3')
        # print(type(h3))  # => <class 'bs4.element.Tag'>，為一個對象
        print(h3.text)  # 這樣才是h3標籤的文本內容，類型為字符串
        img_url = "http:" + a.find("img").attrs.get("src")
        print(img_url)

        # ---------下載圖片---------
        # img_response = requests.get(img_url)
        # with open("test.jpg", "wb") as f:
        #     f.write(img_response.content)  # response.content 返回資料數據類型為bytes
