from django.shortcuts import render
from django.template import RequestContext
import simplejson as simplejson
from iPlop.beerpong.models import Team, Game


def PlayGame(request, game, cups_removed):
    if game is None:
        game = Game(team_a=Team.objects.get(pk=1), team_b=Team.objects.get(pk=2))
    else:
        if game.current_team == Team.objects.get(pk=1):
            game.team_a_cups_left -= cups_removed
        else:
            game.team_b_cups_left -= cups_removed
        if game.current_team == 0:
            game.winner = game.current_team
            game.status = False
        return simplejson.dumps(game)

