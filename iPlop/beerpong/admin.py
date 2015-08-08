from django.contrib import admin
from iPlop.beerpong.models import Game, Player, Team


class GameAdmin(admin.ModelAdmin):
    list_display = ['team_a', 'team_b']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','player1', 'player2']


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'location']


admin.site.register(Game, GameAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
