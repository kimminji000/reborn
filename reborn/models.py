from django.db import models

# Create your models here.
class Partner(models.Model):
    name = models.CharField(max_length=10)
    explain = models.CharField(max_length=50)
    field = models.CharField(max_length=10)
    img = models.ImageField(upload_to='partner/')

    def __str__(self):
        return self.name