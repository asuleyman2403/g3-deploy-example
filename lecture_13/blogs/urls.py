from django.urls import path
from blogs.views import index_page, create_blog, blog_details, delete_blog, blogs_post_create, delete_post

urlpatterns = [
    path('', index_page, name='index'),
    path('blogs/create/', create_blog, name='create_blog'),
    path('blogs/<int:pk>/', blog_details, name='blog_details'),
    path('blogs/<int:pk>/delete/', delete_blog, name='delete_blog'),
    path('blogs/<int:pk>/posts-create', blogs_post_create, name='blogs_post_create'),
    path('posts/<int:pk>/delete', delete_post, name='delete_post')
]
