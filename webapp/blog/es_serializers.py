from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from blog.es_documents import BlogDocument


class BlogDocumentSimpleSerializer(DocumentSerializer):
    class Meta:
        document = BlogDocument
        fields = (
            'title',
            'body',
            'created',
        )
