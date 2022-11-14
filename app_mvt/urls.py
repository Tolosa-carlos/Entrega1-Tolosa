from django.urls import path
from app_mvt.views import *

urlpatterns = [
    path("", inicio, name="app-inicio")
]