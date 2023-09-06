from django.db import models

class job(models.Model):
    posting_date=models.IntegerField()
    qualification=models.CharField(max_length=10)
    offer_sal=models.FloatField()
    location=models.TextField(max_length=30)
    #image= models.ImageField(upload_to="images/")