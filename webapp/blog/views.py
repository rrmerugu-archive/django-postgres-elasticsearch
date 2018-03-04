from blog.serializers import BlogModelSerializer
from blog.models import Blog
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    pagination_class = PageNumberPagination
