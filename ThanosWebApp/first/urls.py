from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('tapped/', tapped_view),
]