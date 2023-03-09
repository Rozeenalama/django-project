from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('contactus',contact, name='contactus'),
    path('portfolio', portfolio, name='portfolio'),
    path('price', price, name='price'),
    path('services', services, name='services'),
    path('aboutus', about, name='aboutus'),

]

