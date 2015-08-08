import datetime
from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    gender = models.CharField(max_length=120)
    location = models.CharField(max_length=120)


class Team(models.Model):
    player1 = models.ForeignKey(Player)
    player2 = models.ForeignKey(Player, related_name='player2')
    name = models.CharField(max_length=120)


class Game(models.Model):
    team_a = models.ForeignKey(Team, default=None)
    team_b = models.ForeignKey(Team, related_name='team_b')
    date_played = models.DateTimeField(default=100)
    winner = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    current_team = models.IntegerField(default=1)
    team_a_cups_left = models.IntegerField(default=10)
    team_b_cups_left = models.IntegerField(default=10)