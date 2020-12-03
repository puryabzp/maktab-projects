from django.shortcuts import render
from .models import Post, Category, PostSetting, Comment, CommentLike
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader
from django.urls import reverse


def all_posts(request):
    author = request.GET.get('author', None)
    posts = Post.objects.all()
    if author:
        posts = posts.filter(author__username=author)

    category = request.GET.get('category', None)
    if category:
        posts = Post.objects.filter(category__title=category)

    context = {
        'posts': posts
    }
    return render(request, 'blog/posts.html', context)


def single_post(request, slug):
    post = Post.objects.select_related('post_setting', 'category').get(slug=slug)
    context = {
        'post': post,
        'post_setting': post.post_setting,
        'category': post.category,
        'comments': post.comments.all()
    }
    return render(request, 'blog/post_single.html', context)

    # try:
    #     posts = Post.objects.get(slug=slug)
    # except:
    #     raise Http404("Not Found!")
    #
    # html = "<html><head><title>this is a post</title></head><body><h1>{}</h1><p>{}</p><a href = {}>show posts Of
    # this " \ "categories</a></body></html> ".format(posts.title, posts.content, reverse("category_posts",
    # kwargs={"slug": posts.category.slug})) return HttpResponse(html)


def category_posts(request, slug):
    posts = Post.objects.filter(category__slug=slug)
    string = ""
    link = reverse("posts_archive")
    html = "<li>title : {}  , content: {}   , <a href={}>click for see all posts</a> </li>"
    for obj in posts:
        string += html.format(obj.title, obj.content, link)
        string = "<ul>" + string + "</ul>"
    return HttpResponse(string)


def show_categories(request):
    categories = Category.objects.all()
    string = ""
    html = "<li><a href={}>{}</a></li>"
    for obj in categories:
        string += html.format(reverse("category_posts", kwargs={"slug": obj.slug}), obj.title)
        string = "<ul>" + string + "</ul><a href={}>Back home</a>".format(reverse('main_page'))
    return HttpResponse(string)


def main_page(request):
    html = "<html><head><title></title></head><body><p>Want to see Categories:</p><a href={" \
           "}>Categories</a></br><p>Want to see Posts:</p><a href={}>Posts</a></html>".format(
        reverse("show_categories"), reverse("posts_archive"))
    return HttpResponse(html)


def author_posts(request, slug):
    posts = Post.objects.filter(author__username=slug)
    html = "<li>title : {}  , content: {}   , <a href={}>click for see all posts</a> </li>"
    string = ""
    for post in posts:
        string += html.format(post.title, post.content, "link")
        string = "<ul>" + string + "</ul>"
    return HttpResponse(string)

# Create your views here.
# def home(request):
#     posts = Post.objects.all()
#     string = ' , '.join([post.title for post in posts])
#     return HttpResponse(string)
#
#
# def single(requset, slug): try: posts = Post.objects.get(slug=slug) except Post.DoesNotExist: raise Http404() link
# = reverse('posts_archive') blog = '<html><head><title>purya bzp</title></head><body><h1>{}</h1><p>{}</p><a href={
# }>link</a></body></html'.format( posts.title, posts.content, link) return HttpResponse(blog)
#

# def show_categories(request):
#     category_posts = reverse('categories_posts')
#     posts = Post.objects.all()
#     categories = [post.category.title for post in posts]
#     string = ""
#     html = "<a href = {}>{}</a>"
#     for post in categories:
#         string += html.format(category_posts, categories[post])
#     return HttpResponse(string)
#
#
# def show_categories_posts(request, category):
#     post_lists = reverse('posts_archive')
#     string = ""
#     posts = Post.objects.filter(category__slug=category)
#     category_posts = '<li><a href={}>{}</a></li>'
#     for obj in posts:
#         string += category_posts.format(post_lists, obj.title)
#         string = "<ul>" + string + "</ul>"
#
#     return HttpResponse(string)
#
# def show_categories(request):
#     category_posts = reverse('categories_posts')
#     posts = Post.objects.all()
#     string = ' , '.join([post.category.title for post in posts])
#     return HttpResponse(string)
