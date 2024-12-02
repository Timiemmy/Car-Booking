from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q
from datetime import datetime, timedelta
from .models import Booking
from .serializers import BookingSerializer


class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        # Get the vehicle and booking dates from request
        vehicle_id = request.data.get('vehicle')
        pickup_date = request.data.get('pickup_date')
        pickup_time = request.data.get('pickup_time')
        trip_duration = request.data.get('trip_duration')

        # Combine date and time
        pickup_datetime = datetime.strptime(f"{pickup_date} {pickup_time}", "%Y-%m-%d %H:%M")
        end_datetime = pickup_datetime + timedelta(hours=int(trip_duration))

        # Check for overlapping bookings
        existing_bookings = Booking.objects.filter(
            vehicle_id=vehicle_id
        ).filter(
            Q(
                # New booking overlaps with existing booking
                (Q(pickup_date=pickup_date) & Q(pickup_time__lte=pickup_time) & Q(pickup_time__lt=end_datetime.strftime('%H:%M'))) |
                # Existing booking overlaps with new booking
                (Q(pickup_date=pickup_date) & Q(pickup_time__gte=pickup_time) & Q(pickup_time__lt=end_datetime.strftime('%H:%M')))
            )
        )

        if existing_bookings.exists():
            return Response(
                {"error": "Vehicle not available for the selected time. Please choose another beautiful vehicle."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # If vehicle is available, proceed with creating the booking
        return super().create(request, *args, **kwargs)



class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer