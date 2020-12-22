from django.urls import path
from django.views.decorators.http import require_POST
from django.views.generic import ArchiveIndexView

from blog.models import Post
from blog.views import main_page, LikeComment, PostsView, SinglePost, CreateComment, Categories, CategoryPosts, \
    AuthorsPosts, ArticleMonthArchiveView, ArticleWeekArchiveView,show_month,show_week

urlpatterns = [

    path('posts/<slug:slug>/', SinglePost.as_view(), name='single_post'),
    path('categories/<slug:slug>/', CategoryPosts.as_view(), name="category_posts"),
    path('categories/', Categories.as_view(), name='show_categories'),
    path('', main_page, name="main_page"),
    path('like_comment/', LikeComment.as_view(), name='like_comment'),
    path('posts/', PostsView.as_view(), name='posts_archive'),
    path('comment/', CreateComment.as_view(), name='comment_create'),
    path('authors/<slug:slug>/', AuthorsPosts.as_view(), name="authors_posts"),
    path('latest/', ArchiveIndexView.as_view(model=Post, date_field='create_at', template_name='blog/posts.html',
                                             context_object_name='post_list'),
         name="latest_posts"),
    path('monthly/<int:year>/<int:month>/', ArticleMonthArchiveView.as_view(month_format='%m'),
         name="archive_month_numeric"),
    path('<int:year>/week/<int:week>/', ArticleWeekArchiveView.as_view(), name="archive_week"),
    path('show_month/', show_month, name='show_month'),
    path('show_week/', show_week, name='show_week'),

]
