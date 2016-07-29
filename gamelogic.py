#!python3

ONE_WALL_CHANCE = 20.00
TWO_WALL_CHANCE = 5.00
THREE_WALL_CHANCE = 0.00
FOUR_WALL_CHANCE = 0.00

PLAYER_STARTING_POSITION = (0,0)

BOARD_SIZE = 10
TOTAL_POINTS = 20

import cell
import random

class Gamelogic():
    def __init__(self):

        #initialize teams by recieving team names
        self.teams = []
        self.number_of_teams = input("enter number of teams")
        for i in range(self.number_of_teams):
            self.teams.append(cell.Team("team" + str(i)))

        #initialize board size
        self.board = BoardHandler.generateBoard(BOARD_SIZE)

        #initialize player
        self.playerx,self.playery = PLAYER_STARTING_POSITION

        #initialize turn marker
        self.currentturn = 0

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
            if self.playery == 0 or self.board[playery][playerx].wallup or self.board[playery-1][playerx].walldown:
                #invalid move
                print("invalid move")

            else:
                self.playery-=1
        elif turnstring == "down":
            #check if down is a valid move
            #"down" : y+=1
            if self.playery == BOARD_SIZE or self.board[playery][playerx].walldown or self.board[playery+1][playerx].wallup:
                #invalid move
                print("invalid move")
            else:
                self.playery+=1
    
        elif turnstring == "left":
            #check if left is a valid move
            #"left" : x-=1
            if self.playerx == 0 or self.board[playery][playerx].wallleft or self.board[playery][playerx-1].wallright:
                #invalid move
                print("invalid move")
            else:
                self.playerx-=1
    
        elif turnstring == "right":
            #check if right is a valid move
            if self.playerx == BOARD_SIZE or self.board[playery][playerx].wallright or self.board[playery][playerx+1].wallleft:
                print("invalid move")
            else:
                self.playerx+=1
    
        elif turnstring == "idle":
            pass

        if turnstring != "idle":
            self.checkforpoints()

        #shift turn marker
        self.currentturn+=1
        if self.currentturn == self.number_of_teams:
            self.currentturn = 0

    def checkforpoints(self):
        if self.board[playery][playerx].iscontainpoint:
            self.board[playery][playerx].removePoint()
            self.teams[self.currentturn].addScore()

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
        board[dim-1][dim-1].setFinish()

        #generate points
        temp = coordlist.copy()
        temp.remove((dim-1,dim-1))
        temp.remove(PLAYER_STARTING_POSITION)


        temp2 = random.sample(coordlist, TOTAL_POINTS)

        for x,y in temp2:
            board[y][x].placePoint()
        #generated points

        #generate walls
        temp = ['left','right','up','down']
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                d = {}
                
                if not board[y][x].isfinish and (x,y) != PLAYER_STARTING_POSITION:
                    
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

                    
                
