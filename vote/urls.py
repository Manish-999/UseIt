from django.urls import path
from vote.views import start,pool,result

app_name='vote'

urlpatterns = [
    path('',start,name="index"),
    path('pool',pool,name="pool"),
    path('result',result,name="result")
]