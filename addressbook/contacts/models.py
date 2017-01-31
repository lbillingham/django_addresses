from django.urls import reverse
from django.db import models
from django.db.models.functions import Lower


class Contact(models.Model):
    max_name_len = 255
    first_name = models.CharField(
        max_length=max_name_len,
    )
    last_name = models.CharField(
        max_length=max_name_len,
    )

    email = models.EmailField()

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        _str = ' '.join([self.first_name, self.last_name])
        return _str

    @classmethod
    def field_names(cls):
        """return field names as strings"""
        reserved_field_names = ['id']
        field_names = [f.name for f in cls._meta.get_fields()]
        wanted = [n for n in field_names if n not in reserved_field_names]
        return wanted

    def get_absolute_url(self):
       return reverse('contacts-view', kwargs={'pk': self.id})

class Address(models.Model):

    contact = models.OneToOneField(Contact)
    address_type = models.CharField(
        max_length=10,
    )

    address = models.CharField(
        max_length=255,
    )
    city = models.CharField(
        max_length=255,
    )
    state = models.CharField(
        max_length=2,
    )
    postal_code = models.CharField(
        max_length=20,
    )

    class Meta:
        unique_together = ('contact', 'address_type',)

    @classmethod
    def field_names(cls):
        """return field names as strings"""
        reserved_field_names = ['id']
        field_names = [f.name for f in cls._meta.get_fields()]
        wanted = [n for n in field_names if n not in reserved_field_names]
        return wanted
