import requests
from bs4 import BeautifulSoup

"""
response.cookies: 返回cookies對象
response.cookies.get_dict(): 以字典型式返回cookies

soup.find("td", attrs={"class": "td2"}): 找出指定屬性的標籤對象

知識點:
通常cookies是在登入後服務器傳給我們的，讓他能辨識是否為同一個使用者，而抽屜這個網站是把登入前的cookies在登入成功後
進行驗證，並使之為我們的cookies，而這登入後服務器傳給我們的cookies是用來迷惑我們的。
"""

"""1.登入前的訪問"""
# 帶著請求頭傳過去，讓網站認為你是合法訪問
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "accept": "*/*",
}
get_response = requests.get(
    url="https://dig.chouti.com/",
    headers=headers,
)
get_cookie_dict = get_response.cookies.get_dict()
print("get_cookie_dict", get_cookie_dict)


# 從登入頁面的請求頭(Headers)裡的FormData中找出他的Form欄位
post_dict = {
    "phone": "886918207171",
    "password": "jamie851230",
    "oneMonth": 1,
}
# login/ 是透過post提交，故用requests.post
response = requests.post(
    url="https://dig.chouti.com/login",
    data=post_dict,
    headers=headers,
    # 通常登入時也不會用到cookies，是在登入成功後才會返回cookies，抽屜這是特例
    cookies=get_cookie_dict,
)
login_cookie_dict = response.cookies.get_dict()  # 以字典類型返回cookies
print("login_cookie_dict", login_cookie_dict)


"""2.登入後的訪問"""
# 帶著cookies，讓網站知道是誰登入的，通常是用通常是用login_cookie_dict
response = requests.get(
    url="https://dig.chouti.com/profile",
    headers=headers,
    # 通常是用cookies=login_cookie_dict就可以了，但這個網站卻不行，所以須把cookie一個個拿來測試
    # 思路: 可以透過get和post登入成功後產生的cookies進行比對，
    # 在這發現登入成功後產生的cookies用來騙我們的，而是使用get_cookie_dict
    cookies=get_cookie_dict,
)

"""3.將html文本轉換為BeautifulSoup對象"""
soup = BeautifulSoup(response.text, features="html.parser")
"""4.過濾出想要資料"""
print(soup.find("td", attrs={"class": "td2"}))
