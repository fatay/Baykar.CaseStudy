from rest_framework import serializers
from BaykarApp.models import Category, AirVehicle

# Serialize Category for configuring response

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        
# Serialize AirVehicle for configuring response

class AirVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirVehicle
        fields = ('id', 'category', 'name', 'model_name', 'tail_number', 'iff_code', 'weight')





