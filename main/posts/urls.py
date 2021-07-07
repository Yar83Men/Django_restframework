from django.urls import path, include
from .views import PostsViewSet, RatesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostsViewSet, basename="posts")
router.register('rates', RatesViewSet, basename="rates")


urlpatterns = [
    path('', include(router.urls)),
]
