from django.shortcuts import render
from _db import models


def index_view(request):
    return render(request, 'cabinet/index.html')


def login_view(request):
    return render(request, 'cabinet/login.html')


def logout_view(request):
    return render(request, 'cabinet/logout.html')


def statistic_view(request):
    return render(request, 'cabinet/statistic.html')


def invoice_view(request):
    return render(request, 'cabinet/invoice/index.html')


def invoice_view_view(request):
    return render(request, 'cabinet/invoice/view.html')


def tariffs_view(request):
    return render(request, 'cabinet/tariffs/index.html')


def tariffs_view_view(request):
    return render(request, 'cabinet/tariffs/view.html')


def messages_view(request):
    return render(request, 'cabinet/messages/index.html')


def messages_view_view(request):
    return render(request, 'cabinet/messages/view.html')


def messages_create_view(request):
    return render(request, 'cabinet/messages/create.html')


def messages_delete_view(request):
    return render(request, 'cabinet/messages/delete.html')


def master_request_view(request):
    return render(request, 'cabinet/master-request/index.html')


def master_request_create_view(request):
    return render(request, 'cabinet/master-request/create.html')


def master_request_delete_view(request):
    return render(request, 'cabinet/master-request/delete.html')


def user_view(request):
    return render(request, 'cabinet/user/index.html')


def user_change_view(request):
    return render(request, 'cabinet/user/change.html')