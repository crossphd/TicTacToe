from django.contrib import admin
from app.models import Game, Move


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')
    list_editable = ('status',)

admin.site.register(Game, GameAdmin)
admin.site.register(Move)
