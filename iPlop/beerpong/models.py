import datetime
from django.db import models

class Game(models.Model):
    team_a= models.ForeignKey(Team)
    team_b= models.ForeignKey(Team)
    date_played = models.DateTimeField(default=datetime.datetime.now)
    winner = models.ForeignKey(Team, default=None)
    status = models.BooleanField(default=True)
    current_team = models.ForeignKey(Team, default=team_a)
    team_a_cups_left = models.IntegerField(default=10)
    team_b_cups_left = models.IntegerField(default=10)

class Team(models.Model):
    Player1 = models.ForeignKey(Player)
    Player2 = models.ForeignKey(Player)
    name = models.CharField(max_length=120)

class Player(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    gender = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
