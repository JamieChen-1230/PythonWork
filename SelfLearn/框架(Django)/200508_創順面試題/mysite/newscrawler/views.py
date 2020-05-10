from django.shortcuts import render
from newscrawler import models
import requests
from bs4 import BeautifulSoup


def save(dic, deep_dic, hour_ago):
    new_obj = models.News.objects.filter(**dic).first()
    # 資料已存在就更新，不存在就新增
    if new_obj:
        models.Contents.objects.filter(id=new_obj.content_id).update(**deep_dic)
        dic["hour_ago"] = hour_ago
        models.News.objects.filter(id=new_obj.id).update(**dic)
    else:
        c_obj = models.Contents.objects.create(**deep_dic)
        print(c_obj)
        dic["hour_ago"] = hour_ago
        dic["content"] = c_obj
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
    upload_time = info_div.find("span").text
    print(upload_time)
    # 影片網址
    video_url = content_bs.find("div", class_="video-container").find("iframe").attrs.get("src")
    print(video_url)
    return content, upload_time, video_url


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
        dic = {}
        # 網址
        url = "https://nba.udn.com/" + new.attrs.get('href')
        dic.setdefault("url", url)
        print(url)
        # 圖片網址
        img_url = new.find("img").attrs.get('src')
        dic.setdefault("img_url", img_url)
        print(img_url)
        # 多久前上傳的
        hour_ago = new.find("b").text
        print(hour_ago)
        # 標題
        title = new.find("h3").text
        dic.setdefault("title", title)
        print(title)
        # 大綱
        outline = new.find("p").text
        dic.setdefault("outline", outline)
        print(outline)
        # 內容
        content, upload_time, video_url = deep_crawl(url)
        # 存進DB
        deep_dic = {
            "content": content,
            "upload_time": upload_time,
            "video_url": video_url
        }
        save(dic, deep_dic, hour_ago)


def index(request):
    crawler()
    news_list = models.News.objects.all()
    return render(request, "index.html", locals())


def show_content(request):
    nid = request.GET.get("nid")
    new = models.News.objects.filter(id=nid)[0]
    content_obj = models.Contents.objects.filter(news__id=nid)[0]
    return render(request, "content.html", locals())

