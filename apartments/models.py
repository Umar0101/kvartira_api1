from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


User = get_user_model()


class Amenity(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Apartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apartments', blank=True)
    title = models.CharField(max_length=80)
    description = models.TextField()
    guests = models.IntegerField(default=1)
    bedroom = models.IntegerField(blank=True, null=True)
    bed = models.IntegerField(blank=True, null=True)
    bathroom = models.IntegerField(blank=True, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    cover_photo = models.ImageField(upload_to='apartment/cover_photos',blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    phone_number = PhoneNumberField(region='KG')
    average_rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            self.average_rating = sum(r.value for r in ratings) / ratings.count()
        else:
            self.average_rating = 0 
        self.save(update_fields=['average_rating'])

    def __str__(self):
        return f'{self.title} - {self.user}'

class ApartmentPhoto(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='apartmentphotos')
    photo = models.ImageField(upload_to= 'apartment/photos/', blank=True, null=True)

    def __str__(self):
        return f'Фото - {self.apartment.title}'
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ratings')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='ratings')
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'apartment')

    def __str__(self):
        return f'{self.user} - {self.apartment} - {self.value}'
    
