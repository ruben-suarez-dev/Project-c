from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from http import HTTPStatus as status

from .models import Condominium, House, Inhabitants
from .serializers import CondominiumSerializer, HouseSerializer, InhabitantSerializer

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
    returnStructure = {}
    serializer = CondominiumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        returnStructure['data'] =  serializer.data
        returnStructure['code'] =  '200'
        return Response(returnStructure)
    returnStructure['code'] = '400'
    return Response(returnStructure)


# Api para Actualizar Condominios
@api_view(['PUT', 'POST'])
def edit_condominium(request, pk):
    returnStructure = {}
    try:
        tmp_condominium = Condominium.objects.get(id=pk)
    except Condominium.DoesNotExist:
        returnStructure['code'] = '401'
        return Response(returnStructure)
        
    serializer = CondominiumSerializer(tmp_condominium, data=request.data)
    if serializer.is_valid():
        serializer.save()
        returnStructure['data'] =  serializer.data
        returnStructure['code'] =  '201'
        return Response(returnStructure)
    returnStructure['code'] = '400'
    return Response(returnStructure)

# Api para borra Condominios
@api_view(['DELETE', 'POST'])
def delete_condominium(request, pk):
    returnStructure = {}
    tmp_condominium = Condominium.objects.get(id=pk)
    if tmp_condominium:
        tmp_condominium.delete()
        returnStructure['code'] = '210'
        returnStructure['data'] = pk
        return Response(returnStructure)
    returnStructure['code'] = '400'
    return Response(returnStructure)

# Api para crear casas
@api_view(['POST'])
def add_house(request):
    returnStructure = {}
    serializer = HouseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        returnStructure['data'] =  serializer.data
        returnStructure['code'] =  '200'
        return Response(returnStructure)
    returnStructure['code'] = '400'
    return Response(returnStructure)

# Api para Actualizar casas
@api_view(['PUT', 'POST'])
def edit_house(request, pk):
    returnStructure = {}
    try:
        tmp_house = House.objects.get(id=pk)
    except House.DoesNotExist:
        returnStructure['code'] = '401'
        return Response(returnStructure)
    serializer = HouseSerializer(tmp_house, data=request.data)
    if serializer.is_valid():
        serializer.save()
        returnStructure['data'] =  serializer.data
        returnStructure['code'] =  '201'
        return Response(returnStructure)
    returnStructure['code'] = '400'
    return Response(returnStructure)

# Api para borra Casas
@api_view(['DELETE', 'POST'])
def delete_house(request, pk):
    returnStructure = {}
    tmp_house = House.objects.get(id=pk)
    if tmp_house:
        tmp_house.delete()
        returnStructure['code'] = '210'
        returnStructure['data'] = pk
        return Response(returnStructure)
    returnStructure['code'] = '400'
    return Response(returnStructure)

# Api para Actualizar habitantes
@api_view(['PUT', 'POST'])
def edit_inhabitant(request, pk):
    returnStructure = {}
    try:
        tmp_inhabitant = Inhabitants.objects.get(id=pk)
    except Inhabitants.DoesNotExist:
        returnStructure['code'] = '401'
        return Response(returnStructure)
        
    serializer = InhabitantSerializer(tmp_inhabitant, data=request.data)
    if serializer.is_valid():
        serializer.save()
        returnStructure['data'] =  serializer.data
        returnStructure['code'] =  '201'
        return Response(returnStructure)
    returnStructure['code'] = '400'
    return Response(returnStructure)

# Api para crear Habitantes de una casa
@api_view(['POST'])
def add_inhabitant(request):
    returnStructure = {}
    serializer = InhabitantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        returnStructure['data'] =  serializer.data
        returnStructure['code'] =  '200'
        return Response(returnStructure)
    returnStructure['code'] = '400'
    return Response(returnStructure)

# Api para borra habitantes de una casa
@api_view(['DELETE', 'POST'])
def delete_inhabitant(request, pk):
    returnStructure = {}
    tmp_inhabitant = Inhabitants.objects.get(id=pk)
    if tmp_inhabitant:
        tmp_inhabitant.delete()
        returnStructure['code'] = '210'
        returnStructure['data'] = pk
        return Response(returnStructure)
    returnStructure['code'] = '400'
    return Response(returnStructure)
    

