from django.urls import include, path
from rest_framework import routers

from .views import GetCondominium

urlpatterns = []

router = routers.SimpleRouter()
router.register(r'condominium', GetCondominium, basename="condominium")

urlpatterns += router.urls
