from django.shortcuts import render
from app.models import Game
from django.contrib.auth.decorators import login_required

from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

@login_required
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