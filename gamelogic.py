#!python3

ONE_WALL_CHANCE = 20.00
TWO_WALL_CHANCE = 5.00
THREE_WALL_CHANCE = 0.00
FOUR_WALL_CHANCE = 0.00

PLAYER_STARTING_POSITION = (0,0)
FINISH_POSITION = (9,9)

BOARD_SIZE = 10
TOTAL_POINTS = 20

import cell
import random

class Gamelogic():
    def __init__(self):

        #initialize teams by recieving team names
        self.teams = []
        self.number_of_teams = int(input("enter number of teams"))
        for i in range(self.number_of_teams):
            self.teams.append(cell.Team("team" + str(i)))

        #initialize board size
        self.board = BoardHandler.generateBoard(BOARD_SIZE)

        #initialize player
        self.playerx,self.playery = PLAYER_STARTING_POSITION

        #initialize turn marker
        self.currentteam = 0

        #initialize move history array
        self.movehistory = [("start",PLAYER_STARTING_POSITION)]

    def playerpos(self):
        return (self.playerx,self.playery)

    def isplayer(self,x,y):
        if (x,y) == (self.playerx,self.playery):
            return True
        return False

    def turn(self,turnstring):
        if turnstring == "up":
            #check if up is a valid move
            #"up" : y-=1
            try:
                if self.playery == 0 or self.board[self.playery][self.playerx].wallup or self.board[self.playery-1][self.playerx].walldown:
                    #invalid move
                    print("invalid move")

                else:
                    self.playery-=1
            except IndexError:
                print("invalid move")
        elif turnstring == "down":
            #check if down is a valid move
            #"down" : y+=1
            try:
                if self.playery == BOARD_SIZE or self.board[self.playery][self.playerx].walldown or self.board[self.playery+1][self.playerx].wallup:
                    #invalid move
                    print("invalid move")
                else:
                    self.playery+=1
            except IndexError:
                print("invalid move")
    
        elif turnstring == "left":
            #check if left is a valid move
            #"left" : x-=1
            try:
                if self.playerx == 0 or self.board[self.playery][self.playerx].wallleft or self.board[self.playery][self.playerx-1].wallright:
                    #invalid move
                    print("invalid move")
                else:
                    self.playerx-=1
            except IndexError:
                print("invalid move")
    
        elif turnstring == "right":
            #check if right is a valid move
            try:
                if self.playerx == BOARD_SIZE or self.board[self.playery][self.playerx].wallright or self.board[self.playery][self.playerx+1].wallleft:
                    print("invalid move")
                else:
                    self.playerx+=1
            except IndexError:
                print("invalid move")
    
        elif turnstring == "idle":
            pass

        if turnstring != "idle":
            self.checkforpoints()

        #shift turn marker
        self.currentteam+=1
        if self.currentteam == self.number_of_teams:
            self.currentteam = 0

        self.addmovehistory(turnstring,self.playerpos)

    def addmovehistory(self,turnstring,position):
        self.movehistory.insert(0,(turnstring,position))

    def checkforpoints(self):
        if self.board[self.playery][self.playerx].iscontainpoint:
            self.board[self.playery][self.playerx].removePoint()
            self.teams[self.currentteam].addScore()

class BoardHandler():
    def printBoard(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j],end=",")
            print()

    def generateBoard(dim):
        #create board
        board=cell.initGrid(dim)

        #create a list of all possible coordinates for randoming purposes
        coordlist=[(i,j) for i in range(dim) for j in range(dim)]

        #set finish point
        board[FINISH_POSITION[1]][FINISH_POSITION[0]].setFinish()

        #generate points
        temp = coordlist.copy()
        temp.remove(FINISH_POSITION)
        temp.remove(PLAYER_STARTING_POSITION)


        temp2 = random.sample(temp, TOTAL_POINTS)

        for x,y in temp2:
            board[y][x].placePoint()
        #generated points

        #generate walls
        coordlist2 = coordlist.copy()

        coordlist2.remove(PLAYER_STARTING_POSITION)
        coordlist2.remove(FINISH_POSITION)
        
        temp = ['left','right','up','down']
        for x,y in coordlist2:
            d = {}
                
            if (random.random()*100)<FOUR_WALL_CHANCE:
                #four walls
                for string in temp:
                    d['wall'+string] = True
            elif (random.random()*100)<THREE_WALL_CHANCE:
                #three walls
                t2 = random.sample(temp,3)
                for i in range(3):
                    d['wall'+t2.pop(0)] = True
            elif (random.random()*100)<TWO_WALL_CHANCE:
                #two walls
                t2 = random.sample(temp,2)
                for i in range(2):
                    d['wall'+t2.pop(0)] = True
            elif (random.random()*100)<ONE_WALL_CHANCE:
                #one wall
                t2 = temp.copy()
                for i in range(random.randint(3,7)):
                    random.shuffle(t2)
                d['wall'+t2.pop(0)] = True

            board[y][x].updateWallData(d)
        return board

                    
                
