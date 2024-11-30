from rest_framework.serializers import ModelSerializer,ListField, ImageField
from .models import VehicleImage, Vehicle


class VehicleImageSerializer(ModelSerializer):
    class Meta:
        model = VehicleImage
        fields = ['id', 'image']





class VehicleSerializer(ModelSerializer):
    vehicle_images = VehicleImageSerializer(many=True)
    
    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'model', 
                  'year', 'category', 'description', 
                  'features', 'thumbnail', 'vehicle_images', 'capacity', 'created_at', 'updated_at']
        read_only_fields = ['id', 'vehicle_images', 'created_at', 'updated_at']
