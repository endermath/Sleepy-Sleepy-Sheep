#!/usr/bin/python

import pygame,sys

from general import FPS
from sheep import *


pygame.init()
fpsClock = pygame.time.Clock()
pygame.display.set_caption("Sleepy Sleepy Sheep")

screenSurface = pygame.display.set_mode(800,600)

player = Player()
game = Game()

while True:

    waiting=True
    while waiting:
        # Show main menu
        screenSurface.fill((4,2,12))
        # Wait for space
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                waiting = False
        pygame.display.update()
        fpsClock.tick(FPS)
        
    while not gameOver:
        game.nextLevel()
        while playingLevel:
            game.tick()
            pygame.display.update()
            fpsClock.tick(FPS)
        game.showLevelResults()
    