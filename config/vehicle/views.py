from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Vehicle, VehicleImage
from .serializers import VehicleImageSerializer, VehicleSerializer



class VehicleListCreateView(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'model', 'year']


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class VehicleDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

    

class VehicleImageView(ListCreateAPIView):
    serializer_class = VehicleImageSerializer
    queryset = VehicleImage.objects.all()


class VehicleImageDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleImageSerializer
    queryset = VehicleImage.objects.all()