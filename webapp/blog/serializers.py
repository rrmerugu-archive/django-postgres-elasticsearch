from rest_framework import serializers
from blog.models import Blog


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'created')
