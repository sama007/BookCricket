class GameEngine(object):
    def __init__(self, userid1, userid2, playeridarray1, playeridarray2, maxover):
        super().__init__()
        self.userid1 = userid1
        self.userid2 = userid2
        self.playeridarray1 = playeridarray1
        self.playeridarray2 = playeridarray2
        self.tosswinner = None
        self.battingteam = None
        self.score1 = 0
        self.score2 = 0
        self.deliverycount1 = 0
        self.deliverycount2 = 0
        self.dismissals1 = 0
        self.dismissals2 = 0
        self.currentbatter = None 
        self.currentbowler = None
        self.nonstriker = None
        # self.bowlingteam = None

    def performToss(self):
        self.tosswinner = self.userid1
        return self.tosswinner

    def setBattingteam(self, userid):
        self.battingteam = userid
    
    def getBattingTeam(self):
        return self.battingteam
    
    def getFieldingTeam(self):
        batter = self.getBattingTeam()
        if batter == None:
            return None
        elif self.userid1 == batter:
            return self.userid2
        else:
            return self.userid1
    
    def startGame(self):

