from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from django_elasticsearch_dsl_drf.views import BaseDocumentViewSet
from blog.es_documents import BlogDocument
from blog.es_serializers import BlogDocumentSimpleSerializer


class ESBlogViewSet(BaseDocumentViewSet):
    document = BlogDocument
    serializer_class = BlogDocumentSimpleSerializer
    pagination_class = PageNumberPagination
    paginate_by = 30
