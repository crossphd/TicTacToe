from django.conf.urls import url

import player.views

urlpatterns = [    
    url(r'new_invitation$', player.views.new_invitation, name='player_new_invitation'),
    url(r'$', player.views.home, name='player_home'),
]