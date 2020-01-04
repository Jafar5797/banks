from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse
# Create your models here.
class Suggestion(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    
    def __str__(self):
       return self.content

    def get_absolute_url(self):
    	return reverse('sdetail',kwargs={"id":self.id})
