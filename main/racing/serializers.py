from rest_framework import serializers
from .models import Driver

best_time = 19


class DriverSerializer(serializers.ModelSerializer):
    best_record = serializers.SerializerMethodField('_get_best_record')

    def _get_best_record(self, driver_object):
        global best_time
        round_finish_time = getattr(driver_object, "round_finish_time")
        if round_finish_time and round_finish_time < best_time:
            best_time = round_finish_time
            return best_time
        else:
            return best_time

    class Meta:
        model = Driver
        fields = '__all__'
