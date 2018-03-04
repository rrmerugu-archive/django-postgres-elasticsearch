from rest_framework import routers
from django.conf.urls import url, include
from blog import views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
