from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from .serializers import CarSerializer
from .models import Car, Plan


@api_view()
@permission_classes([AllowAny])
def index(request):
    print(request.query_params)
    return Response({"Message":"Hello DRF"}, status=status.HTTP_200_OK)


class CarViewset(viewsets.ModelViewSet):
    serializer_class = CarSerializer

    def get_queryset(self):
        cars_object = Car.objects.all()
        return cars_object

    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     #print(params)
    #     params_list = params['pk'].split("-")
    #     cars = Car.objects.filter(Q(car_brand=params_list[0]) & Q(car_model=params_list[1]))
    #     serializer = CarSerializer(cars, many=True)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        car_data = request.data
        new_car = Car.objects.create(
            car_brand=car_data['car_brand'],
            car_model=car_data['car_model'],
            production_year = car_data['production_year'],
            car_body = car_data['car_body'],
            engine_type = car_data['engine_type']
        )
        new_car.save()
        serializer = CarSerializer(new_car)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        login_user = request.user
        if login_user == "admin":
            car = self.get_object()
            car.delete()
        else:
            return Response({"message": "Недостаточно прав"})

        return Response({"message":"deleted"})

    # def update(self, request, *args, **kwargs):
    #     car_object = self.get_object()
    #     data = request.data
    #
    #     car_plan = Plan.objects.get(plan_name=data['plan_name'])
    #
    #     car_object.car_plan = car_plan
    #     car_object.car_brand = data['car_brand']
    #     car_object.car_model = data['car_model']
    #     car_object.production_year = data['production_year']
    #     car_object.car_body = data['car_body']
    #     car_object.engine_type = data['engine_type']
    #
    #     car_object.save()
    #
    #     serializer = CarSerializer(car_object)
    #     return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        car_object = Car.objects.get()
        data = request.data

        car_object.car_brand = data.get('car_brand', car_object.car_brand)
        car_object.car_model = data.get('car_model', car_object.car_model)
        car_object.production_year = data.get('car_brand', car_object.production_year)
        car_object.car_body = data.get('car_brand', car_object.car_body)
        car_object.engine_type = data.get('car_brand', car_object.engine_type)

        car_object.save()

        serializer = CarSerializer(car_object)
        return Response(serializer.data)






