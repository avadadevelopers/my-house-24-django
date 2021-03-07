from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import PermissionsMixin, AbstractUser
# from solo.models import SingletonModel
# from embed_video.fields import EmbedVideoField
import os
from . import services, managers
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from abc import ABC, abstractmethod


class Model(models.Model):
    class Meta:
        app_label = '_db'


class CustomAbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    email = models.CharField(
        _('email address'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[],
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = managers.CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class User(CustomAbstractUser):
    about = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        app_label = '_db'


class Telephone(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()
    viber = models.BooleanField(default=False)
    whatsapp = models.BooleanField(default=False)
    telegram = models.BooleanField(default=False)


class House(Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number = models.IntegerField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    image4 = models.ImageField(upload_to='images/')
    image5 = models.ImageField(upload_to='images/')


class Section(Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Floor(Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Measure(Model):
    name = models.CharField(max_length=255)


class Service(Model):
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)


class Meter(Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    counter = models.IntegerField()
    indication_date = models.DateField()
    status = models.CharField(max_length=255)


class Currency(Model):
    name = models.CharField(max_length=255)


class Rate(Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class RateService(Model):
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    price = models.FloatField()


class Account(Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    money = models.FloatField()
    active = models.BooleanField(default=True)


class TransferType(Model):
    name = models.CharField(max_length=255)
    transfer_income = models.BooleanField()


class Transfer(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transfer_type = models.ForeignKey(TransferType, on_delete=models.CASCADE)
    amount = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    payment_made = models.BooleanField()


class Invoice(Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)


class SEO(Model):
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    keywords = models.TextField(null=True)