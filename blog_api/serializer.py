# from rest_framework import serializers
# from blog_api.models import Blog

# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     content = serializers.CharField()
#     published_at = serializers.DateTimeField()

#     def create(self, data):
#         return Blog.objects.create(**data)

from rest_framework import serializers
from blog_api.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'published_at', 'created_at', 'updated_at')