from django.db import models

# Create your models here.

class AjaxModel(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name