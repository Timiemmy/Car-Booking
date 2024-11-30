from django.urls import path
from . import views


app_name = 'vehicle'

urlpatterns = [
    path('images/', views.VehicleImageView.as_view(), name='vehicle_list_image'),
    path('images/<int:pk>/', views.VehicleImageDetailView.as_view(), name='vehicle_image_detail'),
    path('', views.VehicleListCreateView.as_view(), name='vehicle_list'),
    path('<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle_detail'),
]