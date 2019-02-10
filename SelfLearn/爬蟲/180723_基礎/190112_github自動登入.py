import requests
from bs4 import BeautifulSoup

"""1. 訪問登入頁面，並獲取authenticity_token"""
reqGetLogin = requests.get('https://github.com/login')
soupGetLogin = BeautifulSoup(reqGetLogin.text, features='html.parser')
tag = soupGetLogin.find(name='input', attrs={'name': 'authenticity_token'})  # 找出authenticity_token標籤
authenticity_token = tag.get('value')
cookieGetLogin = reqGetLogin.cookies.get_dict()  # 獲取第一次的cookies
reqGetLogin.close()

"""2. 登入github"""
form_data = {
    "authenticity_token": authenticity_token,
    "utf8": "",
    "commit": "Sign in",
    "login": "as124122323@gmail.com",
    'password': 'zx124122323',
}
reqPostLogin = requests.post(
    'https://github.com/session',
    data=form_data,
    cookies=cookieGetLogin
)
cookiePostLogin = reqPostLogin.cookies.get_dict()  # 獲取登入後的cookies
cookieGetLogin.update(cookiePostLogin)  # 第一次的cookies根據登入後的cookies進行更新

"""3. 訪問個人程式碼倉庫"""
reqRepositories = requests.get(
    'https://github.com/settings/repositories',
    cookies=cookieGetLogin,
)
soupRepositories = BeautifulSoup(reqRepositories.text, features='html.parser')

"""4. 過濾資料"""
list_group = soupRepositories.find(name='div', attrs={"data-owner-id": '12606349'}).\
    find(name='div', attrs={"class": 'listgroup js-collaborated-repos mb-4'})
# print(list_group)
from bs4.element import Tag
# print(list(list_group.children))
for child in list_group.children:
    if isinstance(child, Tag):
        project_tag = child.find(name='a', class_='mr-1')  # Owner: silencejamie的專案名
        print(project_tag.string)

