from django.urls import path
# from myapp import views

from myapp.views import home

urlpatterns = [
    path('',home,name='home'),
]

