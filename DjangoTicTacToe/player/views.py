from django.shortcuts import render, redirect
from app.models import Game
from player.models import Invitation
from django.contrib.auth.decorators import login_required

from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from .forms import InvitationForm

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

@login_required
def new_invitation(request):
    if request.method == "POST":
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')        
    else:
        form = InvitationForm()
        return render(request, 'player/new_invitation_form.html', {'form': form})