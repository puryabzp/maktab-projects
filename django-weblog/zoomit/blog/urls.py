from django.urls import path
from django.views.decorators.http import require_POST

from blog.views import main_page, LikeComment, PostsView, SinglePost, CreateComment, Categories,CategoryPosts,AuthorsPosts

urlpatterns = [

    path('posts/<slug:slug>/', SinglePost.as_view(), name='single_post'),
    path('categories/<slug:slug>/', CategoryPosts.as_view(), name="category_posts"),
    path('categories/', Categories.as_view(), name='show_categories'),
    path('', main_page, name="main_page"),
    path('like_comment/', LikeComment.as_view(), name='like_comment'),
    path('posts/', PostsView.as_view(), name='posts_archive'),
    path('comment/', CreateComment.as_view(), name='comment_create'),
    path('authors/<slug:slug>/', AuthorsPosts.as_view(), name="authors_posts"),

]
