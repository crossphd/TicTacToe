from django.shortcuts import render
from app.models import Game

from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    assert isinstance(request, HttpRequest)

    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()

    return render(
        request,
        'player/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'games': active_games,
        }
    )