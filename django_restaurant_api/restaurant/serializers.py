from dataclasses import fields
from rest_framework import serializers
from .models import Restaurant


# create a serializer
class RestaurantSerializer(serializers.Serializer):
    # initialize model and fields you want to serialize
    class Meta:
        model = Restaurant
        fields = ('name', 'time_minutes', 'ingredients')
