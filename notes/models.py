from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime

class WriteNotes(models.Model):
   user =models.ForeignKey(User,related_name='note',on_delete=models.CASCADE)
   topic=models.CharField(max_length=50,null=False)
   date=models.DateTimeField(default=datetime.now)
   data=models.TextField(null=True,blank=True)

   def __str__(self):
      return self.user.username