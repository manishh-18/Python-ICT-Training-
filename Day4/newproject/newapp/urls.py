from django.urls import path

from newapp.views import home

urlpatterns = [
    path('', home, name="url_home"),
]