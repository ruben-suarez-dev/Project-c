from django.contrib import admin

from .models import Condominium, House, Inhabitants

# Register your models here.
admin.site.register(Condominium)
admin.site.register(Inhabitants)
admin.site.register(House)
