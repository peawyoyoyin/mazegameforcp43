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
        teams = []
        number_of_teams = input("enter number of teams")
        for i in range(number_of_teams:
            teams.append(cell.Team("team" + str(i)))

        #initialize board size
        self.board = BoardHandler.generateBoard(BOARD_SIZE)

        #initialize player
        self.playerx,self.playery = self.playerpos = PLAYER_STARTING_POSITION
        

    def isplayer(self,x,y):
        if (x,y) == (self.playerx,self.playery):
            return True
        return False

    def turn(self,turnstring):
        if turnstring == "up":
            #check if up is a valid move
            #"up" : y-=1
            if playery == 0 or board[playery][playerx].wallup or board[playery-1][playerx].walldown:
                #invalid move
                print("invalid move")

            else:
                playery-=1
        elif turnstring == "down":
            #check if down is a valid move
            #"down" : y+=1
            if playery == BOARD_SIZE or board[playery][playerx].walldown or board[playery+1][playerx].wallup:
                #invalid move
                print("invalid move")
    
        elif turnstring == "left":
            #check if left is a valid move
            pass
    
        elif turnstring == "right":
            #check if right is a valid move
            pass
    
        elif turnstring == "idle":
            #stay idle
            pass

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
                
                if not board[y][x].isfinish:
                    
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

                    
                
