from datetime import *

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView, WeekArchiveView

from django.shortcuts import render, redirect
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin, CreateView, BaseCreateView
from django.views.generic.list import BaseListView, MultipleObjectTemplateResponseMixin

from .models import Post, Category, Comment, CommentLike
from django.http import HttpResponse, Http404

from django.urls import reverse
# from .forms import UserRegistrationForm, CommentForm, LoginForm
from .forms import CommentForm, LikeCommentForm
from django.views.generic import ListView, DetailView, FormView
from zoomit.settings import TEMPLATES

User = get_user_model()


class PostsView(LoginRequiredMixin, ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'blog/posts.html'


class SinglePost(DetailView):
    model = Post
    template_name = 'blog/post_single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        post = context['post']
        context['comments'] = post.comments.all()
        context['post_setting'] = post.post_setting
        context['form'] = CommentForm
        return context


class CreateComment(FormView):
    form_class = CommentForm
    template_name = 'blog/post_single.html'

    def post(self, request, *args, **kwargs):
        user = request.user
        print(user.has_perm('blog.add_Post'))
        form = CommentForm(request.POST)
        print(request.POST)
        post = Post.objects.get(id=request.POST['post'])
        print(post)
        if form.is_valid():
            content = form.cleaned_data['content']
            post = Post.objects.get(id=request.POST['post'])
            user = request.user
            comment = Comment.objects.create(author=user, post=post, content=content)
            comment.save()
        return redirect('single_post', post.slug)


class CategoryPosts(BaseListView, MultipleObjectTemplateResponseMixin):
    template_name = 'blog/posts.html'
    model = Post

    def get(self, request, *args, **kwargs):
        print(args)
        posts = Post.objects.filter(category__slug=self.kwargs['slug'])
        return render(request, 'blog/posts.html', {'post_list': posts})


class Categories(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'blog/latest.html'


def main_page(request):
    return redirect('posts_archive')


class LikeComment(CreateView):
    template_name = 'blog/post_single.html'
    form_class = LikeCommentForm

    def post(self, request, *args, **kwargs):
        slug = request.POST['post_slug']
        form = self.form_class(request.POST)
        if form.is_valid():
            condition = bool(int(form.cleaned_data['condition']))
            author = request.user
            comment = Comment.objects.get(id=form.cleaned_data['comment'])
            try:
                like = CommentLike.objects.get(author=author, comment=comment)
                like.condition = condition
                slug = request.POST['post_slug']
                like.save()
                return redirect('single_post', slug)

            except CommentLike.DoesNotExist:
                like = CommentLike.objects.create(author=author, comment=comment, condition=condition)
                like.save()
                return redirect('single_post', slug)


class AuthorsPosts(BaseListView, MultipleObjectTemplateResponseMixin):
    model = Post
    template_name = 'blog/posts.html'

    def get(self, request, *args, **kwargs):
        print(kwargs)
        posts = Post.objects.filter(author__full_name=kwargs['slug'])
        return render(request, 'blog/posts.html', {'post_list': posts})


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = "publish_time"
    allow_future = True
    allow_empty = True
    template_name = 'blog/posts.html'
    context_object_name = 'post_list'


class ArticleWeekArchiveView(WeekArchiveView):
    queryset = Post.objects.all()
    date_field = "publish_time"
    week_format = "%W"
    allow_future = True
    allow_empty = True
    template_name = 'blog/posts.html'
    context_object_name = 'post_list'


def show_month(request):
    if request.method == 'POST':
        time = request.POST['monthly']
        real_time = datetime.strptime(time, '%Y-%m-%d')
        return redirect('archive_month_numeric', real_time.year, real_time.month)
    return redirect('posts_archive')


def show_week(request):
    if request.method == 'POST':
        time = request.POST['weekly']
        print(time)
        real_time = datetime.strptime(time, '%Y-%m-%d')
        a = int(real_time.strftime("%W"))
        return redirect('archive_week',real_time.year, a)
