from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

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

User = get_user_model()


class PostsView(LoginRequiredMixin, ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'blog/posts.html'


class SinglePost(PermissionRequiredMixin,DetailView):
    model = Post
    template_name = 'blog/post_single.html'
    permission_required = ('blog.view_comment',)

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
    template_name = 'blog/categories.html'


def main_page(request):
    html = "<html><head><title></title></head><body><p>Want to see Categories:</p><a href={" \
           "}>Categories</a></br><p>Want to see Posts:</p><a href={}>Posts</a></html>".format(
        reverse("show_categories"), reverse("posts_archive"))
    return HttpResponse(html)


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
