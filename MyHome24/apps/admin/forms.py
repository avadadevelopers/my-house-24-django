from django import forms
from django.db.models import Q
from _db import models


class SEOForm(forms.ModelForm):
    class Meta:
        model = models.SEO
        fields = ['title', 'keywords', 'description']
        widgets = {
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
        fields = ['image', 'title', 'description']
        widgets = {
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
        print(user.queryset)
        fields = ['user', 'manager', 'account', 'transfer_type', 'amount', 'comment', 'payment_made']
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
        }


class InvoiceIDCreateForm(forms.ModelForm):

    pass


class InvoiceTitleCreateForm(forms.ModelForm):
    pass


class InvoiceServicesCreateForm(forms.ModelForm):
    pass