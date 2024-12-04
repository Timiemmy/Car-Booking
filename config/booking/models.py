from django.db import models
from vehicle.models import Vehicle
from custom_account.models import CustomUser

class Booking(models.Model):
    class TripType(models.TextChoices):
        ONE_WAY = 'One-Way', 'One-Way'
        ROUND_TRIP = 'Round-Trip', 'Round-Trip'

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=500)
    dropoff_location = models.CharField(max_length=500)
    trip_type = models.CharField(
        max_length=15, choices=TripType.choices, default=TripType.ONE_WAY
    )
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    trip_duration = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.vehicle.name} Booking - {self.user.email}"

    
    def calculate_total_price(self):
        return self.vehicle.price * self.trip_duration


    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)