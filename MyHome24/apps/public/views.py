from django.shortcuts import render
from _db import models


def index_view(request):
    return render(request, 'public/index.html')


def about_view(request):
    return render(request, 'public/about.html')


def services_view(request):
    return render(request, 'public/services.html')


def contact_view(request):
    return render(request, 'public/contact.html')


def error_view(request):
    return render(request, 'public/error.html')