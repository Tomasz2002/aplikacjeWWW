from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<int:pk>/', views.category_detail),
    path('topics/', views.topic_list),
    path('topics/<int:pk>/', views.topic_detail),
    path('categories/<int:pk>/topics/', views.category_topics_list),
    path('users/posts/', views.user_posts_list),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetailGet.as_view()),
    path('posts/update/<int:pk>/', views.PostUpdate.as_view()),
    path('posts/delete/<int:pk>/', views.PostDelete.as_view()),
]