from django.db import models
from utils import checkPlayerJoinedInGameRoom, checkPlayerOnline

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 15)
    userid = models.CharField(max_length = 10, primary_key = True, unique = True)
    password = models.CharField(max_length = 10)
    isonline = models.BooleanField(default= False)
    isjoinedingameroom = models.BooleanField(default= False)
    teamname = models.CharField(max_length = 20)

    def __str__(self):
        return "{%s : %s}" % (self.name, self.userid)

class Player(models.Model):
    CURRENT_ROLE_CHOICES = [
        ('US', 'Unsold'),
        ('SD', 'Sold')
        ('FD', 'Fielding'),
        ('BL', 'Bowling'),
        ('DD', 'Dismissed'),
        ('YB', 'Yet to bat'),
        ('OS', 'On strike'),
        ('NS', 'Non striker')
    ]
    playerid = models.AutoField(primary_key = True)
    userid = models.ForeignKey(User, on_delete= models.CASCADE)
    tournamentid = models.ForeignKey(TournamentRoom, on_delete=models.CASCADE)
    playername = models.CharField(max_length = 15)
    playercurrentrole = models.CharField(max_length = 2, choices = self.CURRENT_ROLE_CHOICES, default = 'US')
    currentscore = models.PositiveSmallIntegerField(default=0)
    totalballsplayed = models.PositiveSmallIntegerField(default=0)
    totaldeliveriesbowled = models.PositiveSmallIntegerField(default=0)
    totalwicketstaken = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "{%s : %s}" % (self.playerid, self.playername)


class TournamentRoom(models.Model):
    TOURNAMENT_TYPE = [
        ('SN', 'Single match'),
        ('MT', 'Multi match')
    ]
    tournamentid = models.SmallAutoField(primary_key = True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()



    
class GameRoom(models.Model):
    gameroomid = models.SmallAutoField(primary_key = True)
    user1 = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    user2 = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()


    
        


