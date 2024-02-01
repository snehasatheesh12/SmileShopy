from django.db import models

# Create your models here.
class Sitesetting(models.Model):
      banner= models.ImageField(upload_to='media',null=True,blank=True)
      caption=models.TextField()