from django.shortcuts import render
from _db import models


def index_view(request):
    return render(request, 'app_cabinet/index.html')


def login_view(request):
    return render(request, 'app_cabinet/login.html')


def logout_view(request):
    return render(request, 'app_cabinet/logout.html')


def statistic_view(request):
    return render(request, 'app_cabinet/statistic.html')


def invoice_view(request):
    return render(request, 'app_cabinet/invoice/index.html')


def invoice_view_view(request):
    return render(request, 'app_cabinet/invoice/view.html')


def tariffs_view(request):
    return render(request, 'app_cabinet/tariffs/index.html')


def tariffs_view_view(request):
    return render(request, 'app_cabinet/tariffs/view.html')


def messages_view(request):
    return render(request, 'app_cabinet/messages/index.html')


def messages_view_view(request):
    return render(request, 'app_cabinet/messages/view.html')


def messages_create_view(request):
    return render(request, 'app_cabinet/messages/create.html')


def messages_delete_view(request):
    return render(request, 'app_cabinet/messages/delete.html')


def master_request_view(request):
    return render(request, 'app_cabinet/master-request/index.html')


def master_request_create_view(request):
    return render(request, 'app_cabinet/master-request/create.html')


def master_request_delete_view(request):
    return render(request, 'app_cabinet/master-request/delete.html')


def user_view(request):
    return render(request, 'app_cabinet/user/index.html')


def user_change_view(request):
    return render(request, 'app_cabinet/user/change.html')