from django.urls import path, include
from rest_framework.routers import DefaultRouter

from racing.views import DriverViewSet

router = DefaultRouter()
router.register("driver", DriverViewSet, basename="driver")

urlpatterns = [
    path('', include(router.urls))
]