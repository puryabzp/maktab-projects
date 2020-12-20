from django.urls import path
from account.views import Login, Logout, RegisterView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
