from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 200)
    body = models.CharField(max_length = 500)
    subscribe = models.BooleanField()
    def __str__(self):
        return self.email
