from rest_framework.serializers import ModelSerializer

from .models import Amenity, Apartment, ApartmentPhoto, Rating

class ApartmentPhotoSerializer(ModelSerializer):
    class Meta:    
        model = ApartmentPhoto
        fields = '__all__'

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__' 

class ApartmentListSerializer(ModelSerializer):    
    class Meta:
        model = Apartment 
        fields = ['title', 'price', 'average_rating', 'cover_photo']

class ApartmentRetriveSerializer(ModelSerializer):
    photos = ApartmentPhotoSerializer(read_only=True, many=True, source= 'apartmentphotos')
    
    class Meta:
        model = Apartment
        exclude =  ['created_at', 'updated_at']

class ApartmentCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'
        read_only_fields = ['average_rating']

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        request = self.context["request"]
        validated_data["user"] = request.user
        rating, created = Rating.objects.update_or_create(
            apartment=validated_data["apartment"],
            user=request.user,
            defaults={"value": validated_data["value"]},
        )
        
        rating.apartment.update_rating()
        return rating



    


    