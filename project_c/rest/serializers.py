from .models import Condominium, House, Inhabitants
from rest_framework import serializers


class CondominiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominium
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class InhabitantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inhabitants
        fields = '__all__'