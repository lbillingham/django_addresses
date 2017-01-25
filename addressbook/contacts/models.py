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
