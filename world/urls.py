from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('map/', views.map, name='map'),
    path('updatedb/', views.update_location, name='updatedb'),
]