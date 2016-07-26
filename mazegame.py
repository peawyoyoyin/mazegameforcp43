#!python3

import pygame

pygame.init()

DISPLAY_SIZE = DISPLAY_WIDTH , DISPLAY_HEIGHT = 800,600
sc = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("CP43 maze game")

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
