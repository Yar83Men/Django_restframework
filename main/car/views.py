from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarModel
from .serializers import CarSerializer


class CarAPIView(APIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        car = CarModel.objects.all()
        return car

    def get(self, request):
        try:
            id = request.query_params['id']
            if id != None:
                car_id = CarModel.objects.filter(pk=id)
                serializer = CarSerializer(car_id, many=True)
                return Response(serializer.data)
        except:
            car = self.get_queryset()
            serializer = CarSerializer(car, many=True)
            return Response(serializer.data)

    def post(self, request):
        car_data = request.data
        new_car = CarModel.objects.create(
            car_brand=car_data['car_brand'],
            car_model=car_data['car_model'],
            production_year=car_data['production_year'],
            car_body=car_data['car_body'],
            engine_type=car_data['engine_type']
        )
        new_car.save()
        serializer = CarSerializer(new_car)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        car_object = CarModel.objects.get()
        data = request.data
        car_object.car_brand = data['car_brand']
        car_object.car_model = data['car_model']
        car_object.production_year = data['production_year']
        car_object.car_body = data['car_body']
        car_object.engine_type = data['engine_type']
        car_object.save()

        serializer = CarSerializer(car_object)

        return Response(serializer.data)