from django.urls import path
from .views import CarAPIView

urlpatterns = [
    path("apiview/", CarAPIView.as_view()),
]