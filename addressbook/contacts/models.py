from django.db import models

# Create your models here.


class Contact(models.Model):
    max_name_len = 255
    first_name = models.CharField(
        max_length=max_name_len,
    )
    last_name = models.CharField(
        max_length=max_name_len,
    )

    email = models.EmailField()

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
