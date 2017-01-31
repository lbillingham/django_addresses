from django.urls import reverse
from django.db import models


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        _str = '{}'.format(self.name)
        return _str

    @classmethod
    def field_names(cls):
        """return field names as strings"""
        reserved_field_names = ['id']
        field_names = [f.name for f in cls._meta.get_fields()]
        wanted = [n for n in field_names if n not in reserved_field_names]
        return wanted

    def get_absolute_url(self):
       return reverse('organisations-view', kwargs={'pk': self.id})

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
        ordering = ('last_name', 'first_name')

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

class BaseAddress(models.Model):

    first_line = models.CharField(
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
        abstract = True


    @classmethod
    def field_names(cls):
        """return field names as strings"""
        reserved_field_names = ['id']
        field_names = [f.name for f in cls._meta.get_fields()]
        wanted = [n for n in field_names if n not in reserved_field_names]
        return wanted

class OrganisationAddress(BaseAddress):
    organisation = models.OneToOneField(Organisation)

class Address(BaseAddress):

    contact = models.OneToOneField(Contact)

