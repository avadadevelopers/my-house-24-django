from django.shortcuts import render
from _db import models


def index_view(request):
    return render(request, 'index.html')