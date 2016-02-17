from __future__ import unicode_literals

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name
        
    