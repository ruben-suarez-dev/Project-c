from django.db import models

# Create your models here.

class Condominium(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name        = 'Condominium'
        verbose_name_plural = 'Condominiums'
        app_label = 'rest'

    def __str__(self):
        return self.name
    
class House(models.Model):
    number = models.CharField(max_length=100)
    condominium = models.ForeignKey(Condominium, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.number

    
class Inhabitants (models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=12)
    areTenant = models.BooleanField()
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

