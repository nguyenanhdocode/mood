from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.home, name='home'),
    path('new_mood/', views.new_mood, name='new_mood'),
    path('remove_mood/<str:pk>/', views.remove_mood, name='remove_mood'),
    path('edit_mood/<str:pk>/', views.edit_mood, name='edit_mood')
]
