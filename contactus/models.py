from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class ContactInfo(models.Model):
    title = models.CharField(max_length=100, default='Untitled', verbose_name='title')
    text = models.TextField(default='', verbose_name='text')

    def __str__(self):
        return self.title

