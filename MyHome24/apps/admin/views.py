from django.shortcuts import render
from _db import models


def index_view(request):
    return render(request, 'index.html')


def update_me_view(request):
    return render(request, 'update-me.html')


def login_view(request):
    return render(request, 'login.html')


def logout_view(request):
    return render(request, 'logout.html')


def account_transaction_view(request):
    return render(request, 'account-transaction/index.html')


def account_transaction_create_view(request):
    return render(request, 'account-transaction/create.html')


def account_transaction_change_view(request):
    return render(request, 'account-transaction/change.html')


def account_transaction_delete_view(request):
    return render(request, 'account-transaction/delete.html')


def invoice_view(request):
    return render(request, 'invoice/index.html')


def invoice_create_view(request):
    return render(request, 'invoice/create.html')


def invoice_copy_view(request):
    return render(request, 'invoice/copy.html')


def invoice_change_view(request):
    return render(request, 'invoice/change.html')


def invoice_delete_view(request):
    return render(request, 'invoice/delete.html')


def account_view(request):
    return render(request, 'account/index.html')


def account_create_view(request):
    return render(request, 'account/create.html')


def account_change_view(request):
    return render(request, 'account/change.html')


def account_delete_view(request):
    return render(request, 'account/delete.html')


def apartment_view(request):
    return render(request, 'apartment/index.html')


def apartment_create_view(request):
    return render(request, 'apartment/create.html')


def apartment_change_view(request):
    return render(request, 'apartment/change.html')


def apartment_delete_view(request):
    return render(request, 'apartment/delete.html')


def user_view(request):
    return render(request, 'user/index.html')


def user_create_view(request):
    return render(request, 'user/create.html')


def user_change_view(request):
    return render(request, 'user/change.html')


def user_delete_view(request):
    return render(request, 'user/delete.html')


def house_view(request):
    return render(request, 'house/index.html')


def house_create_view(request):
    return render(request, 'house/create.html')


def house_change_view(request):
    return render(request, 'house/change.html')


def house_delete_view(request):
    return render(request, 'house/delete.html')


def message_view(request):
    return render(request, 'message/index.html')


def message_create_view(request):
    return render(request, 'message/create.html')


def message_change_view(request):
    return render(request, 'message/change.html')


def message_delete_view(request):
    return render(request, 'message/delete.html')


def master_request_view(request):
    return render(request, 'master-request/index.html')


def master_request_create_view(request):
    return render(request, 'master-request/create.html')


def master_request_change_view(request):
    return render(request, 'master-request/change.html')


def master_request_delete_view(request):
    return render(request, 'master-request/delete.html')


def meter_data_view(request):
    return render(request, 'meter-data/index.html')


def meter_data_create_view(request):
    return render(request, 'meter-data/create.html')


def meter_data_change_view(request):
    return render(request, 'meter-data/change.html')


def meter_data_delete_view(request):
    return render(request, 'meter-data/delete.html')


def website_main_page_view(request):
    return render(request, 'website/main-page.html')


def website_about_view(request):
    return render(request, 'website/about.html')


def website_services_view(request):
    return render(request, 'website/services.html')


def website_tariffs_view(request):
    return render(request, 'website/tariffs.html')


def website_contact_view(request):
    return render(request, 'website/contact.html')


def services_view(request):
    return render(request, 'services/index.html')


def services_add_view(request):
    return render(request, 'services/add.html')


def services_delete_view(request):
    return render(request, 'services/delete.html')


def tariffs_view(request):
    return render(request, 'tariffs/index.html')


def tariffs_create_view(request):
    return render(request, 'tariffs/create.html')


def tariffs_change_view(request):
    return render(request, 'tariffs/change.html')


def tariffs_copy_view(request):
    return render(request, 'tariffs/copy.html')


def tariffs_delete_view(request):
    return render(request, 'tariffs/delete.html')


def user_admin_role_view(request):
    return render(request, 'user-admin/.html')


def user_admin_create_view(request):
    return render(request, 'user-admin/create.html')


def user_admin_change_view(request):
    return render(request, 'user-admin/change.html')


def user_admin_delete_view(request):
    return render(request, 'user-admin/delete.html')


def pay_company_view(request):
    return render(request, 'pay-company.html')


def transaction_purpose_view(request):
    return render(request, 'transaction-purpose/index.html')


def transaction_purpose_create_view(request):
    return render(request, 'transaction-purpose/create.html')


def transaction_purpose_change_view(request):
    return render(request, 'transaction-purpose/change.html')


def transaction_purpose_delete_view(request):
    return render(request, 'transaction-purpose/delete.html')