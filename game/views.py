from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def gamePage(req):
      return render(req,"game/game.html")


@login_required
def tick(req):
   return render(req,"game/tick.html")


@login_required
def rock(req):
   return render(req,"game/rock.html")


@login_required
def color(req):
   return render(req,"game/color.html")

