from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_avatar/', views.change_avatar, name='change_avatar'),
    path('change_password/', views.change_password, name='change_password'),

]
