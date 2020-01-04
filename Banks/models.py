from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

CHOICES = (('','--- Please Select Consultancy Type ---'),('Retainer','Retainer'),('Project','Project'))


class Bank(models.Model):
    name = models.CharField(max_length=50,unique=True)
    consultancy_type = models.CharField(max_length=50,choices=CHOICES)
    is_active = models.BooleanField(default=True)
    spoc = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bankspoc')
    consultants = models.ManyToManyField(User,related_name='bankconsultants')
    
    def __str__(self):
       return self.name

    def get_absolute_url(self):
    	return reverse('bdetail',kwargs={"id":self.id})
