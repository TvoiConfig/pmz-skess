from django.shortcuts import render
from .models import *

def contact(request):
    return render(request, 'contact.html')
