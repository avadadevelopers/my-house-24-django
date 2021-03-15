from django.shortcuts import render
from _db import models
from . import forms
from django.forms import modelformset_factory

def index_view(request):
    return render(request, 'admin/index.html')


def update_me_view(request):
    return render(request, 'admin/update-me.html')


def login_view(request):
    return render(request, 'admin/login.html')


def logout_view(request):
    return render(request, 'admin/logout.html')


def account_transaction_view(request):
    return render(request, 'admin/account-transaction/index.html')


def account_transaction_create_in_view(request):
    # форма уже существует - forms.AccountTransactionForm
    return render(request, 'admin/account-transaction/create/create_in.html')

def account_transaction_create_out_view(request):
    # форма уже существует - forms.AccountTransactionForm
    return render(request, 'admin/account-transaction/create/create_out.html')

def account_transaction_change_view(request):
    # форма уже существует - forms.AccountTransactionForm
    return render(request, 'admin/account-transaction/update.html')


def account_transaction_delete_view(request):
    return render(request, 'admin/account-transaction/delete.html')


def invoice_view(request):
    return render(request, 'admin/invoice/index.html')


def invoice_create_view(request):
    return render(request, 'admin/invoice/create.html')


def invoice_copy_view(request):
    return render(request, 'admin/invoice/copy.html')


def invoice_change_view(request):
    return render(request, 'admin/invoice/change.html')


def invoice_delete_view(request):
    return render(request, 'admin/invoice/delete.html')


def account_view(request):
    return render(request, 'admin/account/index.html')


def account_create_view(request):
    return render(request, 'admin/account/create.html')


def account_change_view(request):
    return render(request, 'admin/account/change.html')


def account_delete_view(request):
    return render(request, 'admin/account/delete.html')


def apartment_view(request):
    return render(request, 'admin/apartment/index.html')


def apartment_create_view(request):
    return render(request, 'admin/apartment/create.html')


def apartment_change_view(request):
    return render(request, 'admin/apartment/change.html')


def apartment_delete_view(request):
    return render(request, 'admin/apartment/delete.html')


def user_view(request):
    return render(request, 'admin/user/index.html')


def user_create_view(request):
    return render(request, 'admin/user/create.html')


def user_change_view(request):
    return render(request, 'admin/user/change.html')


def user_delete_view(request):
    return render(request, 'admin/user/delete.html')


def house_view(request):
    return render(request, 'admin/house/index.html')


def house_create_view(request):
    return render(request, 'admin/house/create.html')


def house_change_view(request):
    return render(request, 'admin/house/change.html')


def house_delete_view(request):
    return render(request, 'admin/house/delete.html')


def message_view(request):
    return render(request, 'admin/message/index.html')


def message_create_view(request):
    return render(request, 'admin/message/create.html')


def message_change_view(request):
    return render(request, 'admin/message/change.html')


def message_delete_view(request):
    return render(request, 'admin/message/delete.html')


def master_request_view(request):
    return render(request, 'admin/master-request/index.html')


def master_request_create_view(request):
    return render(request, 'admin/master-request/create.html')


def master_request_change_view(request):
    return render(request, 'admin/master-request/change.html')


def master_request_delete_view(request):
    return render(request, 'admin/master-request/delete.html')


def meter_data_view(request):
    return render(request, 'admin/meter-data/index.html')


def meter_data_create_view(request):
    return render(request, 'admin/meter-data/create.html')


def meter_data_change_view(request):
    return render(request, 'admin/meter-data/change.html')


def meter_data_delete_view(request):
    return render(request, 'admin/meter-data/delete.html')


def website_main_page_view(request):

    ########################
    # Empty initialization #
    ########################

    form = None
    formset = []
    seo_form = None
    alerts = None

    ##################
    # Models initial #
    ##################

    # Main page instance
    form_instance: models.WebsiteMainPage = models.WebsiteMainPage.get_solo()

    # Seo instance
    if not form_instance.seo:
        form_instance.seo = models.SEO.objects.create()
        form_instance.save()

    # Main page blocks instance
    if models.WebsiteMainPageBlocks.objects.count() == 0:
        models.WebsiteMainPageBlocks.objects.bulk_create(
            [models.WebsiteMainPageBlocks() for i in range(6)]
        )

    formset_instances = models.WebsiteMainPageBlocks.objects.all()

    ###########################
    # Form initial & handling #
    ###########################

    formset = modelformset_factory(
        model=models.WebsiteMainPageBlocks,
        form=forms.WebsiteMainPageBlocksForm,
        fields=['image', 'title', 'description'],
        extra=0,
    )

    if request.method == 'GET':
        form = forms.WebsiteMainPageForm(
            instance=form_instance
        )
        seo_form = forms.SEOForm(
            instance=form_instance.seo
        )
        formset = formset(
            queryset=formset_instances
        )
    elif request.method == 'POST':
        seo_form = forms.SEOForm(request.POST)
        if seo_form.is_valid():
            seo_form.save()

        form = forms.WebsiteMainPageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        formset = formset(data=request.POST)
        for block in formset:
            if block.is_valid():
                block.save()

        # return redirect(redirect_url_name) # with pk
        alerts = ['Запись была сохранена успешно!', ]

    #############
    # Packaging #
    #############

    print(form_instance.photo.url)

    context = {
        'form': form,
        'formset': formset,
        'seo_form': seo_form,
        'alerts': alerts,
        'form_instance': form_instance,
    }
    return render(request, 'admin/website/main-page.html', context)


def website_about_view(request):
    return render(request, 'admin/website/about.html')


def website_services_view(request):
    return render(request, 'admin/website/services.html')


def website_tariffs_view(request):
    return render(request, 'admin/website/tariffs.html')


def website_contact_view(request):
    return render(request, 'admin/website/contact.html')


def services_view(request):
    return render(request, 'admin/services/index.html')


def services_add_view(request):
    return render(request, 'admin/services/add.html')


def services_delete_view(request):
    return render(request, 'admin/services/delete.html')


def tariffs_view(request):
    return render(request, 'admin/tariffs/index.html')


def tariffs_create_view(request):
    return render(request, 'admin/tariffs/create.html')


def tariffs_change_view(request):
    return render(request, 'admin/tariffs/change.html')


def tariffs_copy_view(request):
    return render(request, 'admin/tariffs/copy.html')


def tariffs_delete_view(request):
    return render(request, 'admin/tariffs/delete.html')


def user_admin_role_view(request):
    return render(request, 'admin/user-admin/role.html')

def user_admin_users_list(request):
    return render(request, 'admin/user-admin/list.html')


def user_admin_create_view(request):
    return render(request, 'admin/user-admin/create.html')


def user_admin_change_view(request):
    return render(request, 'admin/user-admin/change.html')


def user_admin_delete_view(request):
    return render(request, 'admin/user-admin/delete.html')


def pay_company_view(request):
    return render(request, 'admin/pay-company.html')


def transaction_purpose_view(request):
    return render(request, 'admin/transaction-purpose/index.html')


def transaction_purpose_create_view(request):
    return render(request, 'admin/transaction-purpose/create.html')


def transaction_purpose_change_view(request):
    return render(request, 'admin/transaction-purpose/change.html')


def transaction_purpose_delete_view(request):
    return render(request, 'admin/transaction-purpose/delete.html')