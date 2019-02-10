from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from repository import models
from django.urls import reverse
from utils.pagination import Pagination
from utils.ajaxpagination import Pagination as aPagination
import json
from datetime import datetime


def index(request, *args, **kwargs):
    """
    首頁主站
    """
    # 文章內建分類列表
    article_type_list = models.Article.type_choices

    # 判斷分類和url
    if kwargs:
        article_type_id = int(kwargs['article_type_id'])
        base_url = reverse('index', kwargs=kwargs)
    else:
        article_type_id = None
        base_url = "/"

    # 分頁
    data_count = models.Article.objects.filter(**kwargs).count()  # 文章數
    current_page = request.GET.get('p')
    print(current_page)
    page_obj = Pagination(data_count, current_page, perPageItemNum=4)
    page_str = page_obj.page_str(base_url)

    # 篩選文章(照nid倒序排列)，並根據頁數不同而改變文章
    article_list = models.Article.objects.filter(**kwargs).order_by('-nid')[page_obj.start():page_obj.end()]
    blog_list = models.Blog.objects.all()[:5]

    return render(request, "index.html", locals())


def home(request, site):
    """
    個人博客主頁
    :param request:
    :param site:  網址前綴名
    :return:
    """
    # 透過select_related()可以將blog與userinfo進行聯表查詢，減少查詢次數
    # (原本要找出blog後，再用blog.user找userinfo，現在能一次出來)
    # blog = models.Blog.objects.filter(site=site).first()
    blog = models.Blog.objects.filter(site=site).select_related('user').first()

    # 若用戶無博客，則回到首頁
    if not blog:
        return redirect("/")

    tag_list = models.Tag.objects.filter(blog=blog)
    # tag_list = models.Tag.objects.filter(blog_id=blog.nid)，兩種都可
    category_list = models.Category.objects.filter(blog=blog)
    # category_list = models.Category.objects.filter(blog_id=blog.nid)，兩種都可

    # 透過原生sql語句對create_time的"年-月"進行group by
    # 日期格式化:
    # sqlite: strftime('%Y-%m', create_time)
    # mysql: date_format(create_time, '%Y-%m')
    # date_list = models.Article.objects.raw(
    #     "select nid, count(nid) as num, strftime('%Y-%m', create_time) as ctime from repository_article where blog_id={} group by strftime('%Y-%m', create_time);".format(blog.nid)
    # )
    # 因為使用了字符串格式化，所以對於原本的%Y和%m要使用%%Y和%%m才行，不然會被當成是要做格式化的字符串
    date_list = models.Article.objects.raw(
        "select nid, count(nid) as num, strftime('%%Y-%%m', create_time) as ctime from repository_article where blog_id=%s group by strftime('%%Y-%%m', create_time);" % blog.nid
    )

    article_list = models.Article.objects.filter(blog=blog).order_by("-nid")
    # 用於判斷登陸的使用者是否是版主
    if request.user.is_authenticated():
        blog_id = request.session.get("user_info").get("blog__nid")
    else:
        blog_id = None
    return render(request, "home.html", locals())


def allocation(request, site, condition, val):
    # blog = models.Blog.objects.filter(site=site).select_related('user').first()
    blog = models.Blog.objects.filter(site=site).first()
    # 若用戶無博客，則回到首頁
    if not blog:
        return redirect("/")
    tag_list = models.Tag.objects.filter(blog=blog)
    category_list = models.Category.objects.filter(blog=blog)
    date_list = models.Article.objects.raw(
        "select nid, count(nid) as num, strftime('%Y-%m', create_time) as ctime from repository_article where blog_id={} group by strftime('%Y-%m', create_time);".format(blog.nid)
    )

    if condition == "tag":
        # tag = models.Tag.objects.filter(nid=val).first()
        # article_list = models.Article.objects.filter(blog=blog, tags=tag).order_by("-nid")
        article_list = models.Article.objects.filter(blog=blog, tags=val).order_by("-nid")  # 多對多
    elif condition == "category":
        # category = models.Category.objects.filter(nid=val).first()
        # article_list = models.Article.objects.filter(blog=blog, category=category).order_by("-nid")
        article_list = models.Article.objects.filter(blog=blog, category_id=val).order_by("-nid")  # 一對多
    elif condition == "date":
        date = val
        article_list = models.Article.objects.filter(blog=blog, create_time__contains=date).order_by("-nid")

    # 用於判斷登陸的使用者是否是版主
    if request.user.is_authenticated():
        blog_id = request.session.get("user_info").get("blog__nid")
    else:
        blog_id = None
    return render(request, "home_summary_list.html", locals())


def detail(request, site, nid):
    # blog = models.Blog.objects.filter(site=site).select_related('user').first()
    blog = models.Blog.objects.filter(site=site).first()
    tag_list = models.Tag.objects.filter(blog=blog)
    category_list = models.Category.objects.filter(blog=blog)
    date_list = models.Article.objects.raw(
        "select nid, count(nid) as num, strftime('%Y-%m', create_time) as ctime from repository_article where blog_id={} group by strftime('%Y-%m', create_time);".format(
            blog.nid)
    )

    # article = models.Article.objects.filter(blog=blog, nid=nid).select_related('category', 'articledetail').first()
    article = models.Article.objects.filter(blog=blog, nid=nid).first()

    # 分頁
    base_url = "/%s/%s.html" % (site, nid)
    # data_count = models.Comment.objects.filter(article=article).count()  舊評論
    data_count = models.Comment.objects.filter(article=article, reply=None).count()
    current_page = request.POST.get('p')
    # print(current_page)
    page_obj = aPagination(data_count, current_page, perPageItemNum=4)
    page_str = page_obj.page_str(base_url)

    # comment_list = models.Comment.objects.filter(article=article).select_related('reply')
    # comment_list = models.Comment.objects.filter(article=article)[page_obj.start():page_obj.end()]  舊評論
    comment_list = models.Comment.objects.filter(article=article).values("nid",
                                                                         "content",
                                                                         "create_time",
                                                                         "reply",
                                                                         "article__nid",
                                                                         "user__nickname")
    comment_dict = {}
    for item in comment_list:
        if item["reply"]:
            item["son"] = True
        else:
            item["son"] = False
        item["child"] = []
        comment_dict[item["nid"]] = item

    result = []
    for k, v in comment_dict.items():
        if comment_dict[k]["reply"]:
            comment_dict[comment_dict[k]["reply"]]["child"].append(v)
        else:
            result.append(v)

    response = menu_tree(result[page_obj.start():page_obj.end()])
    # print(response)
    if current_page:
        response = menu_tree(result[page_obj.start():page_obj.end()])
        return HttpResponse(
            json.dumps({"page_str": page_str, "response": response}, cls=ComplexEncoder))
        # # 舊評論
        # comment_list = models.Comment.objects.filter(article=article).values(
        #     "content", "create_time", "reply", "user")[page_obj.start():page_obj.end()]
        # comment_list = list(comment_list)  # 因為queryset不能直接透過json傳，所以轉成list
        # for row in comment_list:
        #     row.setdefault("nickname", models.UserInfo.objects.filter(nid=row["user"]).first().nickname)
        #     if row["reply"]:
        #         row.setdefault("renickname", models.Comment.objects.filter(nid=row["reply"]).first().user.nickname)
        #
        # return HttpResponse(json.dumps({"comment_list": comment_list, "page_str": page_str}, cls=ComplexEncoder))

    return render(request, "home_detail.html", locals())


# 因為日期格式無法直接被json序列化，故加上此
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)


def menu_tree(result):
    response = ""
    tpl = """
    <div class="comment-item %s">
        <div class="reply-title clearfix">
            <div class="user-info">
                <span>%s</span>
                <span>%s</span>
            </div>
            <div class="reply" style="display: %s">
                <a href="#">回复</a>
            </div>
        </div>
        <div class="reply-body">
            <div class="content">
                %s
            </div>
            <div class="child_content">%s</div>
        </div>
    </div>
    """
    for row in result:
        son = None
        display = "block"
        if row["son"]:
            son = "son"
            display = "none"

        if row["child"]:
            nickname = row['user__nickname']
            content = row["content"]
            child_content = menu_tree(row['child'])
            ctime = row["create_time"]
            response += tpl % (son, nickname, ctime, display, content, child_content)
        else:
            nickname = row['user__nickname']
            content = row["content"]
            child_content = ""
            ctime = row["create_time"]
            response += tpl % (son, nickname, ctime, display, content, child_content)
    return response