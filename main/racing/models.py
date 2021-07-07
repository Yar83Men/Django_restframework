from django.db import models

class Driver(models.Model):
    driver_name = models.CharField(max_length=120)
    car_brand = models.CharField(max_length=100)
    round_finish_time = models.IntegerField(default=0)


    def __str__(self):
        return self.driver_name 
