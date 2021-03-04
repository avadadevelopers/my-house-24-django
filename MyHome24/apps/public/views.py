from django.shortcuts import render
from _db import models


def index_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def services_view(request):
    return render(request, 'services.html')


def contact_view(request):
    return render(request, 'contact.html')


def error_view(request):
    return render(request, 'error.html')