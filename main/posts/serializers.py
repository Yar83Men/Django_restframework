from rest_framework import serializers
from .models import Posts, Rates


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
        depth = 1


class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = '__all__'
