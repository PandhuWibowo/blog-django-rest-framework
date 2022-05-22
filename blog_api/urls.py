from django.contrib import admin
from django.urls import path
from blog_api.views import BlogView, BlogDetailView

urlpatterns = [
    path('', BlogView.as_view(), name='blogs'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
]