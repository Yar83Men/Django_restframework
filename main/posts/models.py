from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=3000)
    rates = models.OneToOneField('Rates', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Rates(models.Model):
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)

