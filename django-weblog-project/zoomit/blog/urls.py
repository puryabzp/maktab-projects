from django.urls import path
from blog.views import all_posts, show_categories, single_post, category_posts, main_page, author_posts, login_view, \
    logout_view, register_view

urlpatterns = [
    path('posts/', all_posts, name='posts_archive'),
    path('posts/<slug:slug>/', single_post, name='single_post'),
    path('categories/<slug:slug>/', category_posts, name="category_posts"),
    path('categories/', show_categories, name='show_categories'),
    path('authors/<slug:slug>', author_posts, name='author_posts'),
    path('', main_page, name="main_page"),
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register/', register_view, name='register'),

]

# single, show_categories,show_categories_posts


# path('categories/', show_categories, name='categories'),
# path('<slug:category>/', show_categories_posts, name='categories_posts'),
# path('<slug:slug>/', single, name='single_post'),
