#!python3

ONE_WALL_CHANCE = 20.00
TWO_WALL_CHANCE = 5.00
THREE_WALL_CHANCE = 0.00
FOUR_WALL_CHANCE = 0.00

BOARD_SIZE = 10
TOTAL_POINTS = 20

import cell
import random

class Gamelogic():
    
    def __init__(self):

        #initialize teams by recieving team names
        teams = []
        Teams = input("enter teams").split()
        number_of_teams = len(Teams)
        for teamname in Teams:
            teams.append(cell.Team(teamname))

        #initialize board size
        self.board = BoardHandler.generateBoard(BOARD_SIZE)

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

                    
                
