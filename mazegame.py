#!python3

import pygame
import cell
import gamelogic

def rendermap(board,gamelogic,position=(20,20)):
    size_box = 50
    distance = 65
    size_line = 2
    size_player = 30
    scoreboard_pos = ((distance*10)+30,position[1])
    scoreboard_size = (200,635)
    #draw scoreboard
    scoreboard = pygame.Surface(scoreboard_size)
    scoreboard.fill((20, 20, 20))
    
    d_line = 40
    for noteam in range(len(gamelogic.teams)):
        if noteam == gamelogic.currentteam:
            pygame.draw.rect(scoreboard,(255,255,255),(10,10+noteam*d_line,180,33),1)
        font = pygame.font.SysFont("Consolas", 28)
        text_team = font.render(str(gamelogic.teams[noteam]), 1, (200, 200, 200))
        scoreboard.blit(text_team, (15,15+noteam*d_line))
        text_score = font.render(str(gamelogic.teams[noteam].score),1,(200,200,200))
        scoreboard.blit(text_score, (scoreboard_size[0]-15-text_score.get_width(),15+noteam*d_line))
    maze.screen.blit(scoreboard,scoreboard_pos)
    #    #draw game board
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            y=position[0]+distance*i
            x=position[1]+distance*j

            
            pygame.draw.polygon(maze.screen,(0, 20, 0),((x,y),(x+size_box,y),(x+size_box,y+size_box),(x,y+size_box)))
            #third stage
            if len(gamelogic.movehistory)>2 and gamelogic.movehistory[2][2] == (j,i):
                pygame.draw.polygon(maze.screen,(0, 100, 0),((x,y),(x+size_box,y),(x+size_box,y+size_box),(x,y+size_box)))
            #second stage

            if len(gamelogic.movehistory)>1 and gamelogic.movehistory[1][2] == (j,i):
                pygame.draw.polygon(maze.screen,(0, 180, 0),((x,y),(x+size_box,y),(x+size_box,y+size_box),(x,y+size_box)))
            #first stage
            if gamelogic.movehistory[0][2] == (j,i):
                pygame.draw.polygon(maze.screen,(0, 250, 0),((x,y),(x+size_box,y),(x+size_box,y+size_box),(x,y+size_box)))
            
            if board[i][j].wallleft == True:
                pygame.draw.line(maze.screen,(0,255,0),(x-(distance-size_box)//2,y),(x-(distance-size_box)//2,y+size_box),size_line)
            if board[i][j].wallright == True:
                pygame.draw.line(maze.screen,(0,255,0),(x+size_box+(distance-size_box)//2,y),(x+size_box+(distance-size_box)//2,y+size_box),size_line)
            if board[i][j].wallup == True:
                pygame.draw.line(maze.screen,(0,255,0),(x,y-(distance-size_box)//2),(x+size_box,y-(distance-size_box)//2),size_line)
            if board[i][j].walldown == True:
                pygame.draw.line(maze.screen,(0,255,0),(x,y+size_box+(distance-size_box)//2),(x+size_box,y+size_box+(distance-size_box)//2),size_line)
            if board[i][j].isfinish == True:
                pygame.draw.circle(maze.screen,(255,0,0),(x+size_box//2,y+size_box//2),20,0)
            if board[i][j].iscontainpoint == True:
                pygame.draw.circle(maze.screen,(0,0,255),(x+size_box//2,y+size_box//2),20,0)
            if gamelogic.isplayer(j,i):
                pygame.draw.polygon(maze.screen,(255,255,0),((x+size_box//2,y+(size_box-size_player)//2),(x+(size_box-size_player)//2,y+size_box//2),(x+size_box//2,y+size_player+(size_box-size_player)//2),(x+size_player+(size_box-size_player)//2,y+size_box//2)))
      

class Game():
    def __init__(self):
        pygame.init()

        DISPLAY_SIZE = DISPLAY_WIDTH , DISPLAY_HEIGHT = 900,675
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        pygame.display.set_caption("CP43maze game")

        self.clock=pygame.time.Clock()
        self.running = True

        self.gl = gamelogic.Gamelogic()
        
    def update(self):
        self.clock.tick(60)
        
        self.screen.fill(0)
        
        rendermap(self.gl.board,self.gl)
        pygame.display.flip()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.gl.turn("up")
                elif event.key == pygame.K_DOWN:
                    self.gl.turn("down")
                elif event.key == pygame.K_LEFT:
                    self.gl.turn("left")
                elif event.key == pygame.K_RIGHT:
                    self.gl.turn("right")
                    


    def quit(self):
        self.running = False
        pygame.quit()


maze = Game()
while maze.running:
    maze.update()
