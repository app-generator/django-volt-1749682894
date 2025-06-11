# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    first name = models.TextField(max_length=255, null=True, blank=True)
    last name = models.TextField(max_length=255, null=True, blank=True)
    company = models.TextField(max_length=255, null=True, blank=True)
    website = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Licenses(models.Model):

    #__Licenses_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    url = models.TextField(max_length=255, null=True, blank=True)
    username = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)
    licenses key = models.TextField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)

    #__Licenses_FIELDS__END

    class Meta:
        verbose_name        = _("Licenses")
        verbose_name_plural = _("Licenses")


class Knowledge Base(models.Model):

    #__Knowledge Base_FIELDS__
    title = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Knowledge Base_FIELDS__END

    class Meta:
        verbose_name        = _("Knowledge Base")
        verbose_name_plural = _("Knowledge Base")


class Hosting(models.Model):

    #__Hosting_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    sftp remote host = models.TextField(max_length=255, null=True, blank=True)
    sftp username = models.TextField(max_length=255, null=True, blank=True)
    sftp port = models.TextField(max_length=255, null=True, blank=True)
    location = models.TextField(max_length=255, null=True, blank=True)

    #__Hosting_FIELDS__END

    class Meta:
        verbose_name        = _("Hosting")
        verbose_name_plural = _("Hosting")


class Plans(models.Model):

    #__Plans_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    ram = models.TextField(max_length=255, null=True, blank=True)
    storage = models.TextField(max_length=255, null=True, blank=True)
    bandwidth = models.TextField(max_length=255, null=True, blank=True)
    location = models.TextField(max_length=255, null=True, blank=True)
    provider = models.TextField(max_length=255, null=True, blank=True)
    os = models.TextField(max_length=255, null=True, blank=True)
    price = models.TextField(max_length=255, null=True, blank=True)

    #__Plans_FIELDS__END

    class Meta:
        verbose_name        = _("Plans")
        verbose_name_plural = _("Plans")



#__MODELS__END
