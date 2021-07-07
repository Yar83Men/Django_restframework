from django.db import models

class CarModel(models.Model):
    car_brand = models.CharField(max_length=150, verbose_name='Брэнд')
    car_model = models.CharField(max_length=100, verbose_name='Модель')
    production_year = models.CharField(max_length=10, verbose_name='Год выпуска')
    car_body = models.CharField(max_length=150, verbose_name='Кузов')
    engine_type = models.CharField(max_length=50, verbose_name='Двигатель')

    def __str__(self):
        return self.car_brand
