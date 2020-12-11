from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Post, Category, PostSetting, Comment, CommentLike
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader
from django.urls import reverse
from .forms import UserRegistrationForm, CommentForm, LoginForm


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
    try:
        post = Post.objects.select_related('post_setting', 'category').get(slug=slug)
    except Post.DoesNotExist:
        raise Http404('page not found')
    context = {
        'post': post,
        'post_setting': post.post_setting,
        'category': post.category,
        'comments': post.comments.all(),
        'form': CommentForm()
    }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            # ===============================with forms.Form
            # content = form.cleaned_data['content']
            # author = request.user
            # comment = Comment.objects.create(author=author, post=post, content=content)
            # comment.save()
        else:
            context['form'] = form
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


def login_view(request):
    context = {}
    # if request.user.is_authenticated:
    #     return redirect('posts_archive')
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user and user.is_active:
    #         login(request, user)
    #         return redirect('posts_archive')
    # else:
    #     pass
    #
    # return render(request, 'blog/form.html', context={})

    if request.user.is_authenticated:
        return redirect('posts_archive')
    if request.method == 'GET':
        form = LoginForm()
        context = {'form': form}
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('posts_archive')
            else:
                context = {'form': form}
    return render(request, 'blog/form.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('posts_archive')


def register_view(request):
    # if request.method == 'GET':
    #     form = UserRegistrationForm()
    #     context = {'form': form}
    # else:
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         email = form.cleaned_data['email']
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
    #         user.set_password(password)
    #         user.save()
    #         return redirect('login')
    #
    #     else:
    #         pass
    #     print(form)
    #     context = {'form': form}

    if request.method == 'GET':
        form = UserRegistrationForm()
        context = {'form': form}
    else:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('login')
        else:
            context = {'form': form}

    return render(request, 'blog/register.html', context=context)


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
