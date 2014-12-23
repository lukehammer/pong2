from django.db import models


class gamePlayer(models.Model):
    name = models.CharField(max_length=250)

    def get_wins(self):
        pass
    def __unicode__(self):
       return self.name


class gameRecord(models.Model):
    player = models.ForeignKey(gamePlayer)
    player_score = models.IntegerField(default = 0)
    computer_score = models.IntegerField(default = 0)


class gameLobby(models.Model):

    def get_winners_circle_list(self):
        ordered_players = {}
        #uses get wins and other stuff to rank players
        return ordered_players

    def __unicode__(self):
       return self.name

