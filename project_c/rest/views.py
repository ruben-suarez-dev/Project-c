from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from http import HTTPStatus as status

from .models import Condominium, House, Inhabitants
from .serializers import CondominiumSerializer, HouseSerializer, InhabitantSerializer

# Create your views here.


class GetCondominium(
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Condominium.objects
    serializer_class = CondominiumSerializer

class GetHouse(
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = House.objects
    serializer_class = HouseSerializer

class GetInhabitant(
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Inhabitants.objects
    serializer_class = InhabitantSerializer

# Api para obtener los habitantes de una casa mediante house id
@api_view(['GET'])
def filter_inhabitant_house(request, id):
    if request.method == 'GET':
        queryset = Inhabitants.objects.filter(house=id)
        if queryset.exists():
            serializer_all = InhabitantSerializer(queryset, many=True)
            return Response(serializer_all.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
