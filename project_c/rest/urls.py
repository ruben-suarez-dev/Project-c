from django.urls import include, path
from rest_framework import routers

from .views import GetCondominium, GetHouse, GetInhabitant, filter_inhabitant_house

urlpatterns = [
    path('inhabitants/<int:id>/', filter_inhabitant_house, name='filter_inhabitant_house'),
]

router = routers.SimpleRouter()
router.register(r'condominium', GetCondominium, basename="condominium")
router.register(r'house', GetHouse, basename="house")
router.register(r'inhabitant', GetInhabitant, basename="inhabitant")

urlpatterns += router.urls
