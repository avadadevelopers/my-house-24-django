from django.shortcuts import render
from _db import models


def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'login.html')


def logout_view(request):
    return render(request, 'logout.html')


def statistic_view(request):
    return render(request, 'statistic.html')


def invoice_view(request):
    return render(request, 'invoice/index.html')


def invoice_view_view(request):
    return render(request, 'invoice/view.html')


def tariffs_view(request):
    return render(request, 'tariffs/index.html')


def tariffs_view_view(request):
    return render(request, 'tariffs/view.html')


def messages_view(request):
    return render(request, 'messages/index.html')


def messages_view_view(request):
    return render(request, 'messages/view.html')


def messages_create_view(request):
    return render(request, 'messages/create.html')


def messages_delete_view(request):
    return render(request, 'messages/delete.html')


def master_request_view(request):
    return render(request, 'master-request/index.html')


def master_request_create_view(request):
    return render(request, 'master-request/create.html')


def master_request_delete_view(request):
    return render(request, 'master-request/delete.html')


def user_view(request):
    return render(request, 'user/index.html')


def user_change_view(request):
    return render(request, 'user/change.html')