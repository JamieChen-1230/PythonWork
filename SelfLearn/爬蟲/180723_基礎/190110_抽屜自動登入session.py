import requests
from bs4 import BeautifulSoup

"""1.實例化session對象(使用session可以讓我們不用煩惱cookies的問題，他會自動幫我們選擇)"""
session = requests.Session()

"""2.登入前的訪問"""
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "accept": "*/*",
}
i1 = session.get(
    url="https://dig.chouti.com/",
    headers=headers
)
i2 = session.post(
    url="https://dig.chouti.com/login",
    data={
        'phone': "886918207171",
        'password': "jamie851230",
        'oneMonth': 1
    },
    headers=headers
)

"""3.登入後的訪問"""
# session會自動調用這確的cookies
i3 = session.get(
    url="https://dig.chouti.com/profile",
    headers=headers
)

"""4.將html文本轉換為BeautifulSoup對象"""
soup = BeautifulSoup(i3.text, features="html.parser")
"""5.過濾出想要資料"""
print(soup.find("td", attrs={"class": "td2"}))
