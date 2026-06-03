from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('hotels/', views.hotel_list, name='hotel_list'),
    path('hotels/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
]