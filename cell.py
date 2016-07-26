#!python3

class Cell():
    def __init__(self,data=None):
        if data != None:
            self.updateCelldata(data)
    def updateCellData(self,data):
        self.wallleft=data.get('walleft',False)
        self.wallright=data.get('wallright',False)
        self.wallup=data.get('wallup',False)
        self.walldown=data.get('walldown',False)
        
        self.isfinish=data.get('isfinish',False)

        self.iscontainpoint=data.get('iscontainpoint',False)

class Team():
    def __init__(self,teamname):
        
        self.teamname=teamname
        self.score=0

    def addScore(self):
        self.score+=1

    def __str__(self):
        return "Team" + self.teamname

def initGrid(dimension,randomdata):
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
