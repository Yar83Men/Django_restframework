from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Driver
from racing.serializers import DriverSerializer


class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        driver = Driver.objects.all()
        return driver

