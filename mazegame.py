#!python3

import pygame
import cell
import gamelogic

def rendermap(grid=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],position=(100,100)):
    size_box = 50
    distance = 70
    size_line = 2
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            y=position[0]+distance*i
            x=position[1]+distance*j
            pygame.draw.polygon(maze.screen,(0, 255, 0),((x,y),(x+size_box,y),(x+size_box,y+size_box),(x,y+size_box)))
            #if grid[i][j].wallleft == True:
            pygame.draw.line(maze.screen,(0,255,0),(x-(distance-size_box)//2,y),(x-(distance-size_box)//2,y+size_box),size_line)
            #if grid[i][j].wallright == True:
            pygame.draw.line(maze.screen,(0,255,0),(x+size_box+(distance-size_box)//2,y),(x+size_box+(distance-size_box)//2,y+size_box),size_line)
            #if grid[i][j].wallup == True:
            pygame.draw.line(maze.screen,(0,255,0),(x,y-(distance-size_box)//2),(x+size_box,y-(distance-size_box)//2),size_line)
            #if grid[i][j].walldown == True:
            pygame.draw.line(maze.screen,(0,255,0),(x,y+size_box+(distance-size_box)//2),(x+size_box,y+size_box+(distance-size_box)//2),size_line)
            #if grid[i][j].isfinish == True:
            pygame.draw.circle(maze.screen,(255,0,0),(x+size_box//2,y+size_box//2),20,0)
            #if grid[i][j].iscontainpoint == True:
            pygame.draw.circle(maze.screen,(0,0,255),(x+size_box//2,y+size_box//2),20,0)
            

class Game():
    def __init__(self):
        pygame.init()

        DISPLAY_SIZE = DISPLAY_WIDTH , DISPLAY_HEIGHT = 600,600
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        pygame.display.set_caption("CP43maze game")

        self.clock=pygame.time.Clock()
        self.running = True
        
    def update(self):
        self.clock.tick(60)
        
        self.screen.fill(0)
<<<<<<< HEAD
        
=======

        rendermap()
>>>>>>> origin/master
        pygame.display.flip()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()


    def quit(self):
        self.running = False
        pygame.quit()


maze = Game()
while maze.running:
    maze.update()
