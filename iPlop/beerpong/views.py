import json
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import simplejson as simplejson
from django.http import JsonResponse, HttpResponse
from iPlop.beerpong.models import Team, Game

game = Game(team_a=Team.objects.get(pk=1,), team_b=Team.objects.get(pk=2,))

@csrf_exempt
def PlayGame(request, cups_removed=0):
    global game
    if request.method == "GET":
        game = Game(team_a=Team.objects.get(pk=1,), team_b=Team.objects.get(pk=2,))
        return JsonResponse(json.dumps(game, default=lambda o: o.__dict__), safe=False)

    if request.method == "POST":
        data = request.body.decode('utf8')
        data = json.loads(data)
        cups_removed = data['cupsRemoved']
        cups_removed = int(cups_removed)
        if game.current_team == game.team_a.pk:
            game.team_a_cups_left -= cups_removed
            game.current_team = game.team_b.pk
        else:
            game.team_b_cups_left -= cups_removed
            game.current_team = game.team_a.pk
    if game.team_a_cups_left == 0 or game.team_b_cups_left == 0:
        game.winner = game.current_team
        game.status = False
    return JsonResponse(json.dumps(game, default=lambda o: o.__dict__), safe=False)

@csrf_exempt
def Blank(request):
    return render(request, 'blank.html')
