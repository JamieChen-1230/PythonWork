import requests
from bs4 import BeautifulSoup
from nba import models

from apscheduler.scheduler import Scheduler
from django.core.cache import cache
# 例項化
sched = Scheduler()


def save(dic, request):
    new_obj = models.News.objects.filter(title=dic.get("title")).first()
    # 資料已存在就不添加
    if new_obj:
        # request.websocket.send(b'The news no change.')
        print("資料已存在")
        return
    request.websocket.send(b'The news changed. Please unload the window.')
    models.News.objects.create(**dic)


def deep_crawl(url):
    # ----------詳細內容----------
    content_res = requests.get(url)
    content_res.encoding = content_res.apparent_encoding
    content_bs = BeautifulSoup(content_res.text, features="lxml")
    # 內容
    content_list = content_bs.find("div", id='story_body_content').find_all('p')
    content = ""
    for c in content_list:
        if c.text and ("Imagesfacebook" not in c.text):
            content += c.text
            # print(content)
    # 上傳時間
    info_div = content_bs.find("div", class_="shareBar__info")
    post_date = info_div.find("span").text
    # print(post_date)
    # 影片網址
    video_url = content_bs.find("div", class_="video-container").find("iframe").attrs.get("src")
    # print(video_url)
    return content, post_date, video_url


def crawler(request):
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
        # print(url)
        # 圖片網址
        img_url = new.find("img").attrs.get('src')
        # print(img_url)
        # 標題
        title = new.find("h3").text
        print(title)
        # 大綱
        outline = new.find("p").text
        # print(outline)
        # 內容
        content, post_date, video_url = deep_crawl(url)
        # 存進DB
        dic = {
            "title": title,
            "outline": outline,
            "url": url,
            "img_url": img_url,
            "content": content,
            "post_date": post_date,
            "video_url": video_url
        }
        save(dic, request)


def main(request):
    # 每隔1分鐘自動執行
    sched.add_interval_job(crawler, seconds=60, args=[request])
    sched.start()
