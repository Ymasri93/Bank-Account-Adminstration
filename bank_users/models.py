from django.db import models
from django.urls import reverse


# Create your models here.
class BankUser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    iban = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('bank_user_edit', kwargs={'pk': self.pk})
