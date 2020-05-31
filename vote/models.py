from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime

class votes(models.Model):
   user =models.ForeignKey(User,related_name='vote',on_delete=models.CASCADE)
   topic=models.CharField(max_length=100,null=False)
   choose1=models.CharField(max_length=50,null=False,default="default option1")
   option1=models.IntegerField(null=True,blank=True)
   choose2=models.CharField(max_length=50,null=False,default="default option2")
   option2=models.IntegerField(null=True,blank=True)
   choose3=models.CharField(max_length=50,null=False,default="default option3")
   option3=models.IntegerField(null=True,blank=True)
   choose4=models.CharField(max_length=50,null=False,default="default option4")
   option4=models.IntegerField(null=True,blank=True)
   applied=models.TextField(null=True,blank=True)
   date=models.DateTimeField(default=datetime.now())

   def __str__(self):
      return self.topic


class record(models.Model):
   user =models.ForeignKey(User,related_name='record',on_delete=models.CASCADE)
   topic=models.CharField(max_length=100,null=False)
   choose1=models.CharField(max_length=50,null=False,default="default option1")
   option1=models.IntegerField(null=True,blank=True)
   choose2=models.CharField(max_length=50,null=False,default="default option2")
   option2=models.IntegerField(null=True,blank=True)
   choose3=models.CharField(max_length=50,null=False,default="default option3")
   option3=models.IntegerField(null=True,blank=True)
   choose4=models.CharField(max_length=50,null=False,default="default option4")
   option4=models.IntegerField(null=True,blank=True)
   applied=models.TextField(null=True,blank=True)
   date=models.DateTimeField(default=datetime.now())

   def __str__(self):
         return self.topic