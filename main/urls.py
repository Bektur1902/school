from django.urls import path
from .views import *



urlpatterns = [
    path('', HomeSchool.as_view(), name='home'),
    path('days/', Days.as_view(), name='days'),
]