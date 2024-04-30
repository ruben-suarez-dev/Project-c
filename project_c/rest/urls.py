from django.urls import include, path
from rest_framework import routers

from .views import *

urlpatterns = [
    path('inhabitants/<int:id>/', filter_inhabitant_house, name='filter_inhabitant_house'),
    path('houses/<int:id>/', filter_house_condominium, name='filter_house_condominium'),
    path('create-condominium/', add_condominium, name='create-condominium'),
    path('create-house/', add_house, name='create-house'),
    path('create-inhabitant/', add_inhabitant, name='create-inhabitant'),
    path('delete-condominium/<int:pk>/', delete_condominium, name='delete-condominium'),
    path('delete-house/<int:pk>/', delete_house, name='delete-house'),
    path('delete-inhabitant/<int:pk>/', delete_inhabitant, name='delete-inhabitant'),
    path('edit-condominium/<int:pk>/', edit_condominium, name='edit-condominium'),
    path('edit-house/<int:pk>/', edit_house, name='edit-house'),
    path('edit-inhabitant/<int:pk>/', edit_inhabitant, name='edit-inhabitant'),
]

router = routers.SimpleRouter()
router.register(r'condominium', GetCondominium, basename="condominium")
router.register(r'house', GetHouse, basename="house")
router.register(r'inhabitant', GetInhabitant, basename="inhabitant")

urlpatterns += router.urls
