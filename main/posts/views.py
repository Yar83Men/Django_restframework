
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Posts, Rates
from .serializers import PostSerializer, RatesSerializer


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        posts = Posts.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data
        new_rate = Rates.objects.create(
            likes=post_data['rates']['likes'],
            dislikes=post_data['rates']['dislikes'])
        new_rate.save()

        new_post = Posts.objects.create(
            title=post_data['title'],
            body=post_data['body'],
            rates=new_rate
        )
        new_post.save()

        serializer = PostSerializer(new_post)
        return Response(serializer.data)


class RatesViewSet(viewsets.ModelViewSet):
    serializer_class = RatesSerializer

    def get_queryset(self):
        rates = Rates.objects.all()
        return rates
