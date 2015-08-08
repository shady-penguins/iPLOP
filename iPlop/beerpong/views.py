import json
from django.shortcuts import render
from django.template import RequestContext
import simplejson as simplejson
from django.http import JsonResponse, HttpResponse
from iPlop.beerpong.models import Team, Game


def PlayGame(request, game=None, cups_removed=0):
    if request.method == "GET":
        game = Game(team_a=Team.objects.get(pk=1,), team_b=Team.objects.get(pk=2,))
        return JsonResponse(json.dumps(game, default=lambda o: o.__dict__), safe=False)

    if request.method == "POST":
        if game.current_team == game.team_a:
            game.team_a_cups_left -= cups_removed
            game.current_team = game.team_pk
        else:
            game.team_b_cups_left -= cups_removed
            game.current_team = game.team_a.pk
        if game.team_a_cups_left == 0 or game.team_b_cups_left == 0:
            game.winner = game.current_team
            game.status = False
    return JsonResponse(json.dumps(game, default=lambda o: o.__dict__), safe=False)

def Blank(request):
    return render(request, 'blank.html')