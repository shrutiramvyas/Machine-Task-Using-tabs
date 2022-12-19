from django.db import models

# Create your models here.
class Albert(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField(default=0)

    def __str__(self):
        return self.name

class Nikola(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField(default=0)

    def __str__(self):
        return self.name

class Raman(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField(default=0)

    def __str__(self):
        return self.name