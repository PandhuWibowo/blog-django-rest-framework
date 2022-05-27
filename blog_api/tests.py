from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Create your tests here.
class TestBlogApi(APITestCase):
    # List of Blogs
    def test_should_ok_when_get_list_of_blogs(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_be_array_when_get_list_of_blogs(self):
        response = self.client.get(reverse('blogs'))
        self.assertIsInstance(response.data, list)

    # Create Blog
    def test_should_ok_when_create_blog(self):
        data = {
            'title': 'Test',
            'content': 'Test Content'
        }
        response = self.client.post(reverse('blogs'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_be_object_when_create_blog(self):
        data = {
            'title': 'Test',
            'content': 'Test Content'
        }
        response = self.client.post(reverse('blogs'), data)
        self.assertIsInstance(response.data, dict)

    # Blog Detail
    def test_should_ok_when_get_blog_detail(self):
        response = self.client.get(reverse('blog-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_be_object_when_get_blog_detail(self):
        response = self.client.get(reverse('blog-detail', args=[1]))
        self.assertIsInstance(response.data, dict)

    # Update Blog
    def test_should_ok_when_update_blog(self):
        data = {
            'title': 'Test',
            'content': 'Test Content'
        }
        response = self.client.put(reverse('blog-detail', args=[1]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_should_be_object_when_update_blog(self):
        data = {
            'title': 'Test',
            'content': 'Test Content'
        }
        response = self.client.put(reverse('blog-detail', args=[1]), data)
        self.assertIsInstance(response.data, dict)
    
    # Delete Blog
    def test_should_ok_when_delete_blog(self):
        response = self.client.delete(reverse('blog-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_be_empty_when_delete_blog(self):
        response = self.client.delete(reverse('blog-detail', args=[1]))
        self.assertEqual(response.data, {'message': 'Blog not found'})

    def test_should_be_empty_when_delete_blog_not_found(self):
        response = self.client.delete(reverse('blog-detail', args=[100]))
        self.assertEqual(response.data, {'message': 'Blog not found'})