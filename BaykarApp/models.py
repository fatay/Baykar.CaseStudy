from django.db import models

# Create model for category of the air vehicle
      
class Category(models.Model):
      id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=120)

# Create model for air vehicle

class AirVehicle(models.Model):
      id = models.AutoField(primary_key=True)
      category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
      name = models.CharField(max_length=400)
      model_name = models.CharField(max_length=120)
      tail_number = models.CharField(max_length=10)
      iff_code = models.IntegerField()
      weight = models.FloatField()