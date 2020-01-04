from django.db import models

class NewPlot(models.Model):
    plotno=models.IntegerField(primary_key=True)
    roadnumber=models.IntegerField()
    surveyno=models.IntegerField()
    costsqare=models.IntegerField()
    otherexpences=models.IntegerField()
    boundaries=models.IntegerField()
    facing=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    totalcost=models.IntegerField()

class  Appartment(models.Model):
    apartname=models.CharField(max_length=40)
    apartno=models.IntegerField(primary_key="True")
    noofplats=models.IntegerField()
    costofplat=models.FloatField()
    noofvacant=models.IntegerField()