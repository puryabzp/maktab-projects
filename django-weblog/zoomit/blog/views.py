from datetime import *
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import MonthArchiveView, WeekArchiveView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, BaseFormView
from django.views.generic.list import BaseListView, MultipleObjectTemplateResponseMixin
from .models import Post, Category, Comment, CommentLike
from .forms import CommentForm, LikeCommentForm
from django.views.generic import ListView, DetailView, FormView

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


class ShowMonthly(BaseFormView):

    def post(self, request, *args, **kwargs):
        input_time = request.POST['monthly']
        real_time = datetime.strptime(input_time, '%Y-%m-%d')
        return redirect('archive_month_numeric', real_time.year, real_time.month)


class ShowWeekly(BaseFormView):

    def post(self, request, *args, **kwargs):
        input_time = request.POST['weekly']
        print(input_time)
        real_time = datetime.strptime(input_time, '%Y-%m-%d')
        a = int(real_time.strftime("%W"))
        return redirect('archive_week', real_time.year, a)


class SearchField(ListView):
    template_name = 'base/header.html'
    model = Post

    def post(self, request, *args, **kwargs):
        search = request.POST['search']
        print(search)
        if not search:
            return render(request, 'blog/empty_search.html', {})
        object_list = Post.objects.filter(Q(content__icontains=search) | Q(title__icontains=search))
        if not object_list:
            return render(request, 'blog/not_found.html', {})
        return render(request, 'blog/posts.html', {'post_list': object_list})

