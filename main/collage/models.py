from django.db import models


class Modules(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    room = models.IntegerField()

    def __str__(self):
        return self.name


class Pupil(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    grade = models.IntegerField()
    modules = models.ManyToManyField(Modules)


    def __str__(self):
        return self.name