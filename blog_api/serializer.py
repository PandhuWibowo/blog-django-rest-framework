from rest_framework import serializers
from blog_api.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'published_at', 'created_at', 'updated_at')