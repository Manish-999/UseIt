from django import forms
from django.contrib.auth.models import User
from notes.models import WriteNotes

class Userform(forms.ModelForm):

   class Meta:
      model=User
      fields=('username','email','password','first_name','last_name')



class WriteNotesForm(forms.ModelForm):
   class Meta:
      model=WriteNotes
      fields=('topic','data')
