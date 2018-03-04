from blog.serializers import BlogModelSerializer
from blog.models import Blog
from rest_framework import viewsets


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
