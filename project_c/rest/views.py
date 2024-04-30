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
        queryset = Inhabitants.objects.filter(house=id)
        if queryset.exists():
            serializer_all = InhabitantSerializer(queryset, many=True)
            return Response(serializer_all.data)
        return Response(status=status.HTTP_400_NOT_FOUND)

# Api para obtener las casas de un condominio
@api_view(['GET'])
def filter_house_condominium(request, id):
        queryset = House.objects.filter(condominium=id)
        if queryset.exists():
            serializer_all = HouseSerializer(queryset, many=True)
            return Response(serializer_all.data)
        return Response(status=status.HTTP_400_NOT_FOUND)

# Api para crear Condominios
@api_view(['POST'])
def add_condominium(request):
    serializer = CondominiumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Api para Actualizar Condominios
@api_view(['PUT'])
def edit_condominium(request, pk):
    try:
        tmp_condominium = Condominium.objects.get(id=pk)
    except Condominium.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)
        
    serializer = CondominiumSerializer(tmp_condominium, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_EDITED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Api para borra Condominios
@api_view(['DELETE'])
def delete_condominium(request, pk):
    tmp_condominium = Condominium.objects.get(id=pk)
    if tmp_condominium:
        tmp_condominium.delete()
        return Response(status=status.HTTP_200_DELETED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Api para crear casas
@api_view(['POST'])
def add_house(request):
    serializer = HouseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Api para Actualizar casas
@api_view(['PUT'])
def edit_house(request, pk):
    try:
        tmp_house = House.objects.get(id=pk)
    except House.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)
        
    serializer = HouseSerializer(tmp_house, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_EDITED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Api para borra Casas
@api_view(['DELETE'])
def delete_house(request, pk):
    tmp_house = House.objects.get(id=pk)
    if tmp_house:
        tmp_house.delete()
        return Response(status=status.HTTP_200_DELETED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Api para Actualizar habitantes
@api_view(['PUT'])
def edit_inhabitant(request, pk):
    try:
        tmp_inhabitant = Inhabitants.objects.get(id=pk)
    except Inhabitants.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)
        
    serializer = InhabitantSerializer(tmp_inhabitant, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_EDITED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Api para crear Habitantes de una casa
@api_view(['POST'])
def add_inhabitant(request):
    serializer = InhabitantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('Los datos del habitante son: ', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Api para borra habitantes de una casa
@api_view(['DELETE'])
def delete_inhabitant(request, pk):
    tmp_inhabitant = Inhabitants.objects.get(id=pk)
    if tmp_inhabitant:
        tmp_inhabitant.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    

