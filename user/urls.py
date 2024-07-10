from django.urls import path
from user.views import *

urlpatterns = [
    path('create/', create_polyabron, name='create_polyabron'),
    path('list_polyabron/', list_polyabron, name='list_polyabron'),
    path('bosh_vaqtlar/', bosh_vaqtlar, name='bosh_vaqtlar'),
    path('check_availability/', check_availability, name='check_availability'),

]
