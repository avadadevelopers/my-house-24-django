from django import forms
from django.db.models import Q
from _db import models
from datetime import datetime


class SEOForm(forms.ModelForm):
    class Meta:
        model = models.SEO
        fields = ['id', 'title', 'keywords', 'description']
        widgets = {
            'id': forms.HiddenInput(),
            'title': forms.TextInput(attrs={
                'id': 'SEOTitleInput',
                'class': 'form-control',
                'placeholder': 'Введите заголовок',
            }),
            'keywords': forms.TextInput(attrs={
                'id': 'SEOKeywordsInput',
                'class': 'form-control',
                'placeholder': 'Введите ключевые слова',
            }),
            'description': forms.TextInput(attrs={
                'id': 'SEODescriptionInput',
                'class': 'form-control',
                'placeholder': 'Введите описание',
            }),
        }


class WebsiteMainPageForm(forms.ModelForm):
    class Meta:
        model = models.WebsiteMainPage
        fields = ['slide1', 'slide2', 'slide3', 'title', 'description']
        widgets = {
            'slide1': forms.FileInput(attrs={
                'class': 'upload',
                'id': 'File1Input',
            }),
            'slide2': forms.FileInput(attrs={
                'class': 'upload',
                'id': 'File2Input',
            }),
            'slide3': forms.FileInput(attrs={
                'class': 'upload',
                'id': 'File3Input',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок',
                'rows': '3',
            }),
            'description': forms.Textarea(attrs={
                'id': 'DescriptionInput',
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Введите описание',
            }),
        }


class WebsiteMainPageBlocksForm(forms.ModelForm):
    class Meta:
        model = models.WebsiteMainPageBlocks
        fields = ['id', 'image', 'title', 'description']
        widgets = {
            'id': forms.HiddenInput(),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок',
                'rows': '3',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Введите описание',
            }),
        }


class WebsiteTariffsForm(forms.ModelForm):
    class Meta:
        model = models.WebsiteTariffs
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок',
                'rows': '3',
            }),
            'description': forms.Textarea(attrs={
                'id': 'DescriptionInput',
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Введите описание',
            }),
        }


class WebsiteTariffsBlocksForm(forms.ModelForm):
    class Meta:
        model = models.WebsiteTariffBlocks
        fields = ['id', 'image', 'title']
        widgets = {
            'id': forms.HiddenInput(),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок',
                'rows': '3',
            }),
        }


class WebsiteServiceBlocksForm(forms.ModelForm):
    class Meta:
        model = models.WebsiteServiceBlocks
        fields = ['id', 'image', 'name', 'description']
        widgets = {
            'id': forms.HiddenInput(),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название услуги',
                'rows': '3',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Введите описание услуги',
            }),
        }


class WebsiteContactsForm(forms.ModelForm):
    class Meta:
        model = models.WebsiteContacts
        fields = ['id', 'title', 'description', 'site', 'name', 'address', 'tel', 'email', ]
        widgets = {
            'id': forms.HiddenInput(),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Введите описание',
            }),
            'site': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес',
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите электронную почту',
            }),
        }


class AccountTransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transfer
        user = forms.ModelChoiceField(
            queryset=models.User.objects.filter(is_superuser=False),
            empty_label=None,
        )
        manager = forms.ModelChoiceField(
            queryset=models.User.objects.filter(is_superuser=True),
            empty_label=None,
        )
        account = forms.ModelChoiceField(
            queryset=models.Account.objects.all(),
            empty_label=None,
        )
        transfer_type = forms.ModelChoiceField(
            queryset=models.TransferType.objects.all(),
            empty_label=None,
        )
        fields = ['user', 'manager', 'account', 'transfer_type', 'amount', 'comment', 'payment_made', 'created_date']
        widgets = {
            'amount': forms.NumberInput(attrs={
                'id': 'AmountInput',
                'class': 'form-control',
                'placeholder': 'Введите число',
            }),
            'comment': forms.Textarea(attrs={
                'id': 'CommentInput',
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Введите комментарий',
            }),
            'payment_made': forms.CheckboxInput(attrs={
                'id': 'PaymentMadeInput',
                'class': 'form-control',
            }),
            'created_date': forms.DateInput(format=('%Y-%m-%d'), attrs={
                'value': datetime.now().strftime("%Y-%m-%d"),
                'type': "date",
                'class': "form-control",
            }),
        }

class AccountForm(forms.ModelForm):

    class Meta:
        model = models.Account
        house = forms.ModelChoiceField(
            queryset=models.House.objects.all(),
            empty_label=None,
        )

        section = forms.ModelChoiceField(
            queryset=models.Section.objects.all(),
            empty_label=None,
        )

        floor = forms.ModelChoiceField(
            queryset=models.Floor.objects.all(),
            empty_label=None,
        )
        date = datetime.now().strftime('%Y%m%d')
        if models.Account.objects.all().last():
            last_order = models.Account.objects.all().last()
            if last_order.wallet[0:8] == date:
                num = last_order.wallet[8::]
            else:
                num = 1
            date = f'{date}{num}'
        else:
            date = f'{date}1'


        fields = ['status', 'section', 'house', 'floor', 'wallet']
        widgets = {
            'wallet': forms.TextInput(attrs={
                'input_type': 'text',
                'class': 'form-control',
                'value': date,
                'aria-required': 'true'
            }),
        }


class InvoiceIDCreateForm(forms.ModelForm):

    pass


class InvoiceTitleCreateForm(forms.ModelForm):
    pass


class InvoiceServicesCreateForm(forms.ModelForm):
    pass