from django.shortcuts import render, redirect
from repository import models
from ..forms.article import ArticleForm
from ..forms.userInfo import InfoForm
from ..auth.auth import check_login
from django.urls import reverse
from utils.pagination import Pagination


@check_login
def index(request):
    # 要有blog才可使用
    blog_id = request.session['user_info']['blog__nid']
    return render(request, "backend_index.html", locals())


@check_login
def article(request, *args, **kwargs):
    condition = {}

    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    if blog_id is None:
        return redirect("/backend/index.html")
    # --------------------------------------------------

    if kwargs:
        base_url = reverse("article", kwargs=kwargs)
        for k, v in kwargs.items():
            temp = int(v)
            kwargs[k] = temp
            if temp:
                # 不等於0就加入
                condition[k] = temp
    else:
        base_url = "/backend/article-0-0.html"
    # print(base_url)
    condition["blog_id"] = blog_id
    article_type_list = map(lambda item: {'nid': item[0], 'title': item[1]}, models.Article.type_choices)
    category_list = models.Category.objects.filter(blog_id=blog_id)

    # 分頁
    data_count = models.Article.objects.filter(**condition).count()
    current_page = request.GET.get('p')
    page_obj = Pagination(data_count, current_page, perPageItemNum=5)
    page_str = page_obj.page_str(base_url)

    result = models.Article.objects.filter(**condition).order_by("-nid")[page_obj.start():page_obj.end()]
    return render(request, "backend_article.html", locals())


@check_login
def add_article(request):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    if blog_id is None:
        return redirect("/backend/index.html")
    # --------------------------------------------------

    if request.method == "GET":
        obj = ArticleForm(request=request)
        return render(request, "backend_add_article.html", locals())
    elif request.method == "POST":
        obj = ArticleForm(request=request, data=request.POST)
        if obj.is_valid():
            # print(obj.cleaned_data)
            # 無法直接創建的值要先提出來
            tags = obj.cleaned_data.pop('tags')
            content = obj.cleaned_data.pop("content")
            # print(content)
            # 新增文章
            obj.cleaned_data["blog_id"] = request.session["user_info"]["blog__nid"]
            article_obj = models.Article.objects.create(**obj.cleaned_data)
            # 新增標籤和文章對應
            for tag_id in tags:
                tag_id = int(tag_id)
                models.Article2Tag.objects.create(tag_id=tag_id, article_id=article_obj.nid)
            # 新增文章詳細
            models.ArticleDetail.objects.create(content=content, article_id=article_obj.nid)
            return redirect('/backend/article-0-0.html')
        else:
            # print(obj.errors)
            return render(request, "backend_add_article.html", locals())


@check_login
def edit_article(request, nid):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    if blog_id is None:
        return redirect("/backend/index.html")
    # --------------------------------------------------

    blog_id = request.session['user_info']['blog__nid']
    if request.method == "GET":
        article_obj = models.Article.objects.filter(blog_id=blog_id, nid=nid).first()
        if not article_obj:
            return render(request, 'backend_no_article.html')
        tags = article_obj.tags.values_list('nid')
        # print(tags)
        if tags:
            tags = list(zip(*tags))[0]
            # print(tags)
        init_dict = {
            "title": article_obj.title,
            "summary": article_obj.summary,
            "content": article_obj.articledetail.content,
            "article_type_id": article_obj.article_type_id,
            "category_id": article_obj.category_id,
            "tags": tags
        }
        nid = article_obj.nid  # 給等下的form的action中使用
        # print(init_dict)
        obj = ArticleForm(request=request, data=init_dict)
        return render(request, "backend_edit_article.html", locals())
    elif request.method == "POST":
        obj = ArticleForm(request=request, data=request.POST)
        if obj.is_valid():
            # print(obj.cleaned_data)
            tags = obj.cleaned_data.pop("tags")
            content = obj.cleaned_data.pop("content")
            models.Article.objects.filter(nid=nid, blog_id=blog_id).update(**obj.cleaned_data)
            models.ArticleDetail.objects.filter(article_id=nid).update(content=content)
            models.Article2Tag.objects.filter(article_id=nid).delete()
            if tags:
                for tag_id in tags:
                    tag_id = int(tag_id)
                    models.Article2Tag.objects.create(tag_id=tag_id, article_id=nid)
            return redirect('/backend/article-0-0.html')
        else:
            # print(obj.errors)
            return render(request, "backend_edit_article.html", locals())


@check_login
def remove_article(request):
    if request.method == "GET":
        blog_id = request.session['user_info']['blog__nid']
        models.Article.objects.filter(nid=request.GET.get("nid"), blog_id=blog_id).delete()
        return redirect('/backend/article-0-0.html')


@check_login
def category(request):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    if blog_id is None:
        return redirect("/backend/index.html")
    # --------------------------------------------------

    blog_id = request.session["user_info"]["blog__nid"]
    # 分頁
    data_count = models.Category.objects.filter(blog_id=blog_id).count()
    current_page = request.GET.get('p')
    page_obj = Pagination(data_count, current_page, perPageItemNum=7)
    page_str = page_obj.page_str("/backend/category.html")

    result = models.Category.objects.filter(blog_id=blog_id).order_by("nid")[page_obj.start():page_obj.end()]
    return render(request, "backend_category.html", locals())


@check_login
def add_category(request):
    if request.method == "POST":
        title = request.POST.get("title")
        blog_id = request.session["user_info"]["blog__nid"]
        models.Category.objects.create(title=title, blog_id=blog_id)
        return redirect("/backend/category.html")


@check_login
def remove_category(request):
    nid = request.GET.get("nid")
    blog_id = request.session['user_info']['blog__nid']
    models.Category.objects.filter(nid=nid, blog_id=blog_id).delete()
    return redirect("/backend/category.html")


@check_login
def edit_category(request, nid):
    blog_id = request.session['user_info']['blog__nid']
    if request.method == "GET":
        category_obj = models.Category.objects.filter(nid=nid).first()
        title = category_obj.title
        return render(request, "backend_edit_category.html", locals())
    else:
        # print(request.POST)
        title = request.POST.get("title")
        nid = request.POST.get("nid")
        models.Category.objects.filter(nid=nid, blog_id=blog_id).update(title=title)
        return redirect("/backend/category.html")


@check_login
def tag(request):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    if blog_id is None:
        return redirect("/backend/index.html")
    # --------------------------------------------------

    blog_id = request.session["user_info"]["blog__nid"]
    # 分頁
    data_count = models.Tag.objects.filter(blog_id=blog_id).count()
    current_page = request.GET.get("p")
    page_obj = Pagination(data_count, current_page, perPageItemNum=7)
    page_str = page_obj.page_str("/backend/tag.html")

    result = models.Tag.objects.filter(blog_id=blog_id)[page_obj.start():page_obj.end()]
    return render(request, "backend_tag.html", locals())


@check_login
def add_tag(request):
    if request.method == "POST":
        title = request.POST.get("title")
        blog_id = request.session["user_info"]["blog__nid"]
        models.Tag.objects.create(title=title, blog_id=blog_id)
        return redirect("/backend/tag.html")


@check_login
def remove_tag(request):
    nid = request.GET.get("nid")
    blog_id = request.session["user_info"]["blog__nid"]
    models.Tag.objects.filter(nid=nid, blog_id=blog_id).delete()
    return redirect("/backend/tag.html")


@check_login
def edit_tag(request, nid):
    blog_id = request.session["user_info"]["blog__nid"]
    if request.method == "GET":
        tag_obj = models.Tag.objects.filter(nid=nid, blog_id=blog_id).first()
        title = tag_obj.title
        return render(request, "backend_edit_tag.html", locals())
    else:
        nid = request.POST.get("nid")
        title = request.POST.get("title")
        models.Tag.objects.filter(nid=nid, blog_id=blog_id).update(title=title)
        return redirect("/backend/tag.html")


@check_login
def base_info(request):
    theme_dict = {
        "0": "default",
        "1": "warm"
    }
    if request.method == "GET":
        blog_id = request.session["user_info"]["blog__nid"]
        if blog_id:
            # print("yes")
            blog_obj = models.Blog.objects.filter(nid=blog_id).first()
            init_dict = {
                "title": blog_obj.title,
                "site": blog_obj.site,
                # 字典反向查詢
                "theme": list(theme_dict.keys())[list(theme_dict.values()).index(blog_obj.theme)],
            }
            # print(init_dict)
            obj = InfoForm(init_dict)
        else:
            # print("no")
            obj = InfoForm()
        return render(request, "backend_base_info.html", locals())
    else:
        obj = InfoForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            user_id = request.session["user_info"]["nid"]
            obj = models.Blog.objects.filter(user_id=user_id).first()
            theme = theme_dict[request.POST.get("theme")]
            # print(theme)
            blog_dict = {
                "user_id": user_id,
                "title": request.POST.get("title"),
                "site": request.POST.get("site"),
                "theme": theme
            }
            if obj:
                # print("yes")
                models.Blog.objects.filter(nid=obj.nid).update(**blog_dict)
            else:
                # print("no")
                models.Blog.objects.create(**blog_dict)
            return redirect("/login.html")
        else:
            print(obj.errors)
            return render(request, "backend_base_info.html", locals())
