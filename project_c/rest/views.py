from django.shortcuts import render

from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Condominium
from .serializers import CondominiumSerializer

# Create your views here.


class GetCondominium(
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Condominium.objects
    serializer_class = CondominiumSerializer

""" class GetCondominium(APIView):
    def get (self, request):
        queryset = Condominium.objects.all()
        serializer = CondominiumSerializer(queryset, many=True)
        return Response(serializer.data) """