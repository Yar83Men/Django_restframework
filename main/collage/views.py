from rest_framework import viewsets
from rest_framework.response import Response

from collage.models import Pupil, Modules
from collage.serializers import PupilSerializer, ModulesSerializer


class PupilViewSet(viewsets.ModelViewSet):
    serializer_class = PupilSerializer

    def get_queryset(self):
        pupils = Pupil.objects.all()
        return pupils


    def create(self, request, *args, **kwargs):
        data = request.data

        new_pupil = Pupil.objects.create(
            name=data['name'],
            age=data['age'],
            grade=data['grade'],
        )
        new_pupil.save()

        for module in data['modules']:
            module_object = Modules.objects.get(name=module['name'])
            new_pupil.modules.add(module_object)

        serializer = PupilSerializer(new_pupil)
        return Response(serializer.data)


class ModulesViewSet(viewsets.ModelViewSet):
    serializer_class = ModulesSerializer

    def get_queryset(self):
        modules = Modules.objects.all()
        return modules