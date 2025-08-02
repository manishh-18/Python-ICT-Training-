from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll_form, name='poll_form'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
