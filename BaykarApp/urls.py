from django.urls import re_path
from BaykarApp import views

# Configure regex pattern for handling requests.

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^home/$', views.home, name='index'),
    re_path(r'^airvehicle$',views.airVehicleApi),
    re_path(r'^airvehicle/([0-9]+)$', views.airVehicleApi),
    re_path(r'^category$',views.categoryApi),
    re_path(r'^category/([0-9]+)$', views.categoryApi)
]