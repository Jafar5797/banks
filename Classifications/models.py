from django.db import models

# Create your models here.
class Technology_domain(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
       return self.name

class Document_type(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
       return self.name