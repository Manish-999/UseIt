from django.contrib import admin

# Register your models here.
from vote.models import votes,record

admin.site.register(votes)
admin.site.register(record)
