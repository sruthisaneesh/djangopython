from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    descrptn=models.TextField()

    def __str__(self):
        return self.name

class Table(models.Model):
    name=models.CharField(max_length=240)
    place=models.CharField(max_length=250)
    poems=models.TextField()
    image=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
