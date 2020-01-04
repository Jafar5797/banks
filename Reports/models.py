from django.db import models 
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils import timezone as tz
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from tinymce import models as tinymce_models
# Create your models here.


class Report(models.Model):
	spoc = models.ForeignKey(User,on_delete=models.CASCADE,related_name='creator')
	bankname= models.CharField(max_length=30)
	consultants = models.ManyToManyField(User,related_name='consultants')
	date = models.DateField(blank=False,null=False)
	topic= models.TextField()
	technology_domain = models.CharField(max_length=130)
	document_type = models.CharField(max_length=130)
	query= models.TextField()
	response= models.TextField()

	def __str__(self):
		return self.topic


class QueryFiles(models.Model):
	file=models.FileField(upload_to='uploads/',blank=True,)
	report=models.ForeignKey(Report,on_delete=models.CASCADE,related_name='queryfiles',default=None)
	# responsefiles=models.ForeignKey(ResponseFiles,on_delete=models.CASCADE,related_name='responsefiles',default=None)

class ResponseFiles(models.Model):
	file=models.FileField(upload_to='uploads/',blank=True,)
	report=models.ForeignKey(Report,on_delete=models.CASCADE,related_name='responsefiles',default=None)



class Q_Report(models.Model):
	spoc = models.ForeignKey(User,on_delete=models.CASCADE,related_name='gen')
	consultants = models.ManyToManyField(User,related_name='consultants_invovled1')
	bankname= models.CharField(max_length=30)
	fromdate = models.DateField()
	todate = models.DateField()
	requests_recieved = models.TextField(max_length=1200)
	summary_of_response= models.TextField()
	summary_of_workdone = models.TextField()	
	learnings = models.TextField()


	def get_absolute_url(self):
		return reverse('qdetail',kwargs={"id":self.id})



