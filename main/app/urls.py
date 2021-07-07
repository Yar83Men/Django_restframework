from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewset, index

router = DefaultRouter()
router.register("cars", CarViewset, basename='cars')


urlpatterns = [
    path("index/", index),
]
urlpatterns += router.urls
