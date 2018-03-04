from django_elasticsearch_dsl import DocType
from blog.models import Blog
from django.conf import settings

ES_INDEX = settings.ES_INDEX


@ES_INDEX.doc_type
class BlogDocument(DocType):
    class Meta:
        model = Blog  # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'body',
            'created',
        ]
