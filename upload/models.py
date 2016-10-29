from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class NewClinic(models.Model):
    clinic_name = models.CharField(max_length=50)
    def __str__(self):
        return self.clinic_name
