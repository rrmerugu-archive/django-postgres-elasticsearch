from rest_framework import routers
from django.conf.urls import url, include
from blog import views, es_views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^blogs-es$', es_views.ESBlogViewSet.as_view({'get': 'list'}))
]
