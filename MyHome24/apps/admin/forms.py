from django import forms
from django.db.models import Q
from _db import models


class SEOForm(forms.ModelForm):
    class Meta:
        model = models.SEO
        fields = ['title', 'keywords', 'description']
        widgets = {
            'title': forms.Textarea(attrs={
                'id': 'SEOTitleInput',
                'class': 'form-control',
                'placeholder': 'Введите заголовок',
                'rows': '3',
            }),
            'keywords': forms.Textarea(attrs={
                'id': 'SEOKeywordsInput',
                'class': 'form-control',
                'placeholder': 'Введите ключевые слова',
                'rows': '3',
            }),
            'description': forms.Textarea(attrs={
                'id': 'SEODescriptionInput',
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Введите описание',
            }),
        }


class AccountTransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transfer
        user = forms.ModelChoiceField(
            queryset=models.User.objects.filter(Q(is_superuser=False)),
            empty_label=None,
        )
        manager = forms.ModelChoiceField(
            queryset=models.User.objects.filter(Q(is_superuser=True)),
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