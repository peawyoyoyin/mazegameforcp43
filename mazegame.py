#!python3

import pygame
import cell

class Game():
    def __init__(self):
        pygame.init()

        DISPLAY_SIZE = DISPLAY_WIDTH , DISPLAY_HEIGHT = 600,600
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        pygame.display.set_caption("CP43 maze game")

        self.clock=pygame.time.Clock()
        self.running = True
        
    def update(self):
        self.clock.tick(60)
        
        self.screen.fill(0)
        
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
