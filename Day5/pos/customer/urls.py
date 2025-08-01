from django.urls import path
from .views import customer

urlpatterns = [
    path('', customer, name='customer'),
]
