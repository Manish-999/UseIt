from django.urls import path
from game.views import gamePage,tick,rock,color

app_name='game'

urlpatterns = [
    path('', gamePage,name="game"),
    path('tick-tack',tick,name="tick"),
    path('rock-paper',rock,name="rockPaper"),
    path('find-color',color,name="findColor")
]