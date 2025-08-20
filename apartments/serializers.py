from rest_framework.serializers import ModelSerializer

from .models import Amenity, Apartment, ApartmentPhoto

class AmenitySerializer(ModelSerializer):
    model = Amenity
    fields = ['name']

class ApartmentListSerializer(ModelSerializer):
    model = Apartment
    