from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    name = models.CharField(max_length=100, default="Unknown")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='static/porimg', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product.detail', args=[self.pk])
