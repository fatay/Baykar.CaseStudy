from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from BaykarApp.models import Category, AirVehicle
from BaykarApp.serializers import CategorySerializer, AirVehicleSerializer

# API Definations
# Safe property is basically used to inform Django while we were trying to convert JSON to a valid format.

# Air Vehicle API
# Use csrf_exempt for cross-origin policy
@csrf_exempt 
def airVehicleApi(request, id=0):
    
    # GET VEHICLES
    if request.method == 'GET':
        air_vehicles = AirVehicle.objects.all()
        air_vehicle_serializer = AirVehicleSerializer(air_vehicles, many=True)
        return JsonResponse(air_vehicle_serializer.data, safe= False)
    
    # ADD VEHICLE
    elif request.method == 'POST':
        air_vehicle_data = JSONParser().parse(request)
        air_vehicle_serializer = AirVehicleSerializer(data=air_vehicle_data)
        if air_vehicle_serializer.is_valid():
            air_vehicle_serializer.save()
            return JsonResponse("Air Vehicle added successfully.", safe=False)
        return JsonResponse("Failed to add Air Vehicle.", safe=False)

    # UPDATE VEHICLE
    elif request.method == 'PUT':
        air_vehicle_data = JSONParser().parse(request)
        air_vehicle = AirVehicle.objects.get(id = air_vehicle_data["id"])
        air_vehicle_serializer = AirVehicleSerializer(air_vehicle, data=air_vehicle_data)
        if air_vehicle_serializer.is_valid():
            air_vehicle_serializer.save()
            return JsonResponse("Air Vehicle updated successfully.", safe=False)
        return JsonResponse("Failed to update Air Vehicle.")

    # DELETE VEHICLE
    elif request.method == 'DELETE':
        air_vehicle = AirVehicle.objects.get(id = id)
        air_vehicle.delete()
        return JsonResponse("Air Vehicle deleted succesfully.", safe=False)

# Category API
# Use csrf_exempt for cross-origin policy
@csrf_exempt 
def categoryApi(request, id=0):
    
    # GET CATEGORIES
    if request.method == 'GET':
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return JsonResponse(category_serializer.data, safe= False)
    
    # ADD CATEGORY
    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Category added successfully.", safe=False)
        return JsonResponse("Failed to add Category.", safe=False)

    # UPDATE CATEGORY
    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category = Category.objects.get(id = category_data["id"])
        category_serializer = CategorySerializer(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Category updated successfully.", safe=False)
        return JsonResponse("Failed to update Category.")

    # DELETE CATEGORY
    elif request.method == 'DELETE':
        category = Category.objects.get(id = id)
        category.delete()
        return JsonResponse("Category deleted succesfully.", safe=False)
    
# HTML VIEWS

# index
def index(request):
    return render(request, 'index.html', {})

# home
def home(request):
    all_categories = Category.objects.all()
    all_vehicles = AirVehicle.objects.all() 
    return render(request, 'home.html', {'all_categories' : all_categories, 'all_vehicles' : all_vehicles})