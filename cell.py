#!python3

class Cell():
    def __init__(self,data=None):
        if data != None:
            self.wallleft=data.get('wallleft',False)
            self.wallright=data.get('wallright',False)
            self.wallup=data.get('wallup',False)
            self.walldown=data.get('walldown',False)
        else:
            self.wallleft = self.wallright = self.wallup = False
            self.walldown = self.isfinish = self.iscontainpoint = False
    
    def updateWallData(self,data):
        self.wallleft=data.get('wallleft',False)
        self.wallright=data.get('wallright',False)
        self.wallup=data.get('wallup',False)
        self.walldown=data.get('walldown',False)

    def setFinish(self):
        self.isfinish = True

    def placePoint(self):
        self.iscontainpoint = True

    def removePoint(self):
        self.iscontainpoint = False

    def __str__(self):
        if(self.isfinish):
            return "F"
        elif(self.iscontainpoint):
            return "P"
        else:
            return " "

class Team():
    def __init__(self,teamname):
        
        self.teamname=teamname
        self.score=0

    def addScore(self):
        self.score+=1

    def __str__(self):
        return "Team" + self.teamname

def initGrid(dimension):
    Grid = []
    for i in range(0,dimension):
        temp = []
        for j in range(0,dimension):
            temp.append(Cell())
        Grid.append(temp)
    return Grid

def initTeam(teamnames):
    teamArray = []
    for name in teamnames:
        teamArray.append(Team(name))
    return teamArray
