from django.db import models

class Game(models.Model):
    team_a= models.ForeignKey(Team)
    team_b= models.ForeignKey(Team)
    date_played = models.DateTimeField
    winner = models.ForeignKey(Team, default=None)
    score = models.IntegerField()
    status = models.BooleanField(default=True)
    current_team = models.ForeignKey(Team, default=None)
    team_a_cups_left = models.IntegerField()
    team_b_cups_left = models.IntegerField()

class Team(models.Model):
    Player1 = models.ForeignKey(Player)
    Player2 = models.ForeignKey(Player)
    name = models.CharField(max_length=120)

class Player(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    gender = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
