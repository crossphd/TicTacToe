from django.conf.urls import url

import player.views

urlpatterns = [
    url(r'$', player.views.home),
]