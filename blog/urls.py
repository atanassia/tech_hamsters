from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('add/', views.post_add, name='post_add'),
	path('<str:get_username>/', views.post_user, name='post_user'),
	path('<str:get_username>/<slug:posts_slug>/', views.post_user_detail, name='post_user_detail'),
]