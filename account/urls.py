from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   
    path('signup/', views.singup_view, name='signup'),   
    path('user/', views.user_view, name='user'),   
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),   
]