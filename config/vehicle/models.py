from django.db import models



class Vehicle(models.Model):

    class VehicleCategory(models.TextChoices):
        LUXURY = 'Luxury', 'Luxury'
        BUSINESS = 'Business', 'Business'
        ECONOMY = 'Economy', 'Economy'


    name = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    year = models.IntegerField(null=True, blank=True)
    category = models.CharField(
        max_length=100, choices=VehicleCategory.choices)
    description = models.TextField()
    features = models.JSONField(blank=True, null=True)
    capacity = models.PositiveIntegerField(
        help_text='how many weights the car can carry')
    thumbnail = models.ImageField(
        upload_to='vehicles_images/', help_text="Main image for the vehicle")
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text='daily_price for the vehicle')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name


class VehicleImage(models.Model):
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name='vehicle_images')
    image = models.ImageField(upload_to='vehicle_images/gallery')

    def __str__(self) -> str:
        return f"{self.vehicle.name} - image"
