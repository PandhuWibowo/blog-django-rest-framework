from rest_framework.views import APIView
from blog_api.models import Blog
from blog_api.serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework import status

class BlogView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailView(APIView):
    def get(self, request, pk):
        try:
            try:
                blog = Blog.objects.get(pk=pk)
            except:
                return Response({'message': 'Blog not found'}, status=status.HTTP_200_OK)

            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, pk):
        try:
            try:
                blog = Blog.objects.get(pk=pk)
            except:
                return Response({'message': 'Blog not found'}, status=status.HTTP_200_OK)

            serializer = BlogSerializer(blog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, pk):
        try:
            try:
                blog = Blog.objects.get(pk=pk)
            except: 
                return Response({'message': 'Blog not found'}, status=status.HTTP_200_OK)
            
            blog.delete()
            return Response({'message': 'Blog has been deleted'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)