from rest_framework import serializers
from .models import Pupil, Modules


class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = "__all__"


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = "__all__"
        depth = 1