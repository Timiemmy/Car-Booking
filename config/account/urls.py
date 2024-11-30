from django.urls import path
from . import views

app_name = 'account'

urlpatterns=[
    path('', views.UserList.as_view(), name='user_list'),
    path('<int:pk>/', views.UserDetails.as_view(), name='user_detail')
]