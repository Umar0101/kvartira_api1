from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


User = get_user_model()


class Amenity(models.Model):
    name = models.CharField(max_length=200)


class Apartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apartments', blank=True)
    title = models.CharField(max_length=80)
    description = models.TextField()
    guests = models.IntegerField(default=1)
    bedroom = models.IntegerField(blank=True, null=True)
    bed = models.IntegerField(blank=True, null=True)
    bathroom = models.IntegerField(blank=True, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True, many=True)
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    phone_number = PhoneNumberField(region='KG')    

class ApartmentPhoto(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='apartmentphotos')
    photo = models.ImageField(upload_to= 'apartment/photos/', blank=True, null=True)


