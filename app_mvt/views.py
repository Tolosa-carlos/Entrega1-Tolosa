from django.shortcuts import render
from app_mvt.models import *
from app_mvt.forms import *
# Create your views here.


def inicio(request):
    return render(request, "app_mvt/index.html")