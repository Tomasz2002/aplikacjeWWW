from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.topic_list_html, name='topic_list'),
    path('topics/<int:pk>/', views.topic_detail_html, name='topic_detail'),
    path('posts/', views.post_list_html, name='post_list'),
    path('posts/<int:pk>/', views.post_detail_html, name='post_detail'),
    path('topics/<int:pk>/posts/', views.topic_posts_html, name='topic_posts'),
]