from django.shortcuts import render
from .models import *

def about(request):
    return render(request, 'about/about.html')
