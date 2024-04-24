from .models import Condominium
from rest_framework import serializers


class CondominiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominium
        fields = '__all__'