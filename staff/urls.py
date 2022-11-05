
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:pk>', views.Profile, name='profile'),
    path('search/', views.Search, name='search'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
]
