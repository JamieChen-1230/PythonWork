import requests
from bs4 import BeautifulSoup

#
# response = requests.get(url='https://nba.udn.com/nba/index?gr=www')
# response.encoding = response.apparent_encoding
#
# soup = BeautifulSoup(response.text, features="lxml")
# news_body = soup.find("div", id='news_body')
#
# dt_list = news_body.find_all("dt")
#
# news_list = []
# for dt in dt_list:
#     if dt.attrs.get('class'):
#         if "ads" not in dt.attrs.get('class'):
#             news_list.append(dt.find('a'))
#     else:
#         news_list.append(dt.find('a'))
#
# for new in news_list:
#     # 網址
#     url = "https://nba.udn.com/" + new.attrs.get('href')
#     print(url)
#
#     # 圖片網址
#     img_url = new.find("img").attrs.get('src')
#     print(img_url)
#
#     # 多久前上傳的
#     upload_time = new.find("b").text
#     print(upload_time)
#
#     # 標題
#     title = new.find("h3").text
#     print(title)
#
#     # 大綱
#     outline = new.find("p").text
#     print(outline)
#
#     # --------詳細內容----------
#     content_res = requests.get(url)
#     content_res.encoding = content_res.apparent_encoding
#     content_bs = BeautifulSoup(content_res.text, features="lxml")
#
#     # 內容
#     content_list = content_bs.find("div", id='story_body_content').find_all('p')
#     for c in content_list:
#         if c.text and ("Imagesfacebook" not in c.text):
#             content = c.text
#             print(content)
#
#     # 上傳時間
#     info_div = content_bs.find("div", class_="shareBar__info")
#     upload_time = info_div.find("span").text
#     print(upload_time)
#
#     # 影片網址
#     video_url = content_bs.find("div", class_="video-container").find("iframe").attrs.get("src")
#     print(video_url)
#
#     # 下載封面照
#     # img_response = requests.get(img_url)
#     # img_name = title + '.jpg'
#     # with open(img_name, "wb") as f:
#     #     f.write(img_response.content)  # response.content 返回資料數據類型為bytes


def deep_crawl(url):
    # --------詳細內容----------
    content_res = requests.get(url)
    content_res.encoding = content_res.apparent_encoding
    content_bs = BeautifulSoup(content_res.text, features="lxml")
    # 內容
    content_list = content_bs.find("div", id='story_body_content').find_all('p')
    for c in content_list:
        if c.text and ("Imagesfacebook" not in c.text):
            content = c.text
            print(content)
    # 上傳時間
    info_div = content_bs.find("div", class_="shareBar__info")
    upload_time = info_div.find("span").text
    print(upload_time)
    # 影片網址
    video_url = content_bs.find("div", class_="video-container").find("iframe").attrs.get("src")
    print(video_url)


def crawler():
    response = requests.get(url='https://nba.udn.com/nba/index?gr=www')
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, features="lxml")
    news_body = soup.find("div", id='news_body')

    dt_list = news_body.find_all("dt")

    news_list = []
    for dt in dt_list:
        if dt.attrs.get('class'):
            if "ads" not in dt.attrs.get('class'):
                news_list.append(dt.find('a'))
        else:
            news_list.append(dt.find('a'))

    for new in news_list:
        # 網址
        url = "https://nba.udn.com/" + new.attrs.get('href')
        print(url)
        # 圖片網址
        img_url = new.find("img").attrs.get('src')
        print(img_url)
        # 多久前上傳的
        upload_time = new.find("b").text
        print(upload_time)
        # 標題
        title = new.find("h3").text
        print(title)
        # 大綱
        outline = new.find("p").text
        print(outline)
        # 內容
        deep_crawl(url)

# crawler()
