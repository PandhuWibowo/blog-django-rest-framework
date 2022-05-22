from django.contrib import admin
from django.urls import path
from blog_api.views import BlogView, BlogDetailView

urlpatterns = [
    # path('', BlogCreate.as_view()),
    path('', BlogView.as_view()),
    path('<int:pk>', BlogDetailView.as_view()),
]