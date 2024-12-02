from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='user.email', read_only=True)
    vehicle_name = serializers.CharField(source='vehicle.name', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user_email', 'user', 'vehicle', 'vehicle_name', 
                  'pickup_location', 'dropoff_location', 
                  'trip_type', 'pickup_date', 'pickup_time', 'trip_duration', 
                  'total_price', 'is_paid']
        
        read_only_fields = ['total_price', 'is_paid']
