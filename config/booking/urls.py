from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.BookingList.as_view(), name='all_bookings'),
    path('<int:pk>/', views.BookingDetail.as_view(), name='booking_detail'),
]