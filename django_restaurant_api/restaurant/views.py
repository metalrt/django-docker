from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RestaurantSerializer  # import the serializer we just created
from .models import Restaurant


# Create your views here.


class restaurant_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
