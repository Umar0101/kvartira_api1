from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from .models import Apartment, Amenity, ApartmentPhoto, Rating 
from .serializers import AmenitySerializer, RatingSerializer, ApartmentListSerializer, ApartmentCreateUpdateSerializer, ApartmentPhotoSerializer, ApartmentRetriveSerializer
from .permissions import IsActiveUserOrReadOnly

class ApartmentModelViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    permission_classes = [IsActiveUserOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ('title', 'address')

    def get_serializer_class(self):
        if self.action == 'list':
            return ApartmentListSerializer
        elif self.action == 'retrieve':
            return ApartmentRetriveSerializer 
        else:
            return ApartmentCreateUpdateSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user) 

class AmenityModelViewSet(ModelViewSet):
    queryset = Amenity.objects.all()
    permission_classes = [IsActiveUserOrReadOnly]
    serializer_class = AmenitySerializer

class ApartmentPhotoModelViewSet(ModelViewSet):
    queryset = ApartmentPhoto.objects.all()
    permission_classes = [IsActiveUserOrReadOnly]
    serializer_class = ApartmentPhotoSerializer

class RatingModelViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = [RatingSerializer]
    permission_classes = IsActiveUserOrReadOnly

    def perform_create(self, serializer):
        serializer.save()