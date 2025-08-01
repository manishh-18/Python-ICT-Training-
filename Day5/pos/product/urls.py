from django.urls import path
from .views import product

urlpatterns = [
    path('', product, name='product'),
]
