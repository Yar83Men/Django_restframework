from django.urls import path, include
from rest_framework.routers import DefaultRouter

from collage.views import PupilViewSet, ModulesViewSet

router = DefaultRouter()
router.register('pupils', PupilViewSet, basename='pupils')
router.register('modules', ModulesViewSet, basename='pupils')

urlpatterns = [
    path('', include(router.urls))
]