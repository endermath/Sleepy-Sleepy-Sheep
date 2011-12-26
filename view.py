import pygame
from game import *
from decimal import self

class View:
    def __init__(self, gam):
        self.game = gam
        pygame.display.set_caption("Sleepy Sleepy Sheep")
        self.screenSurface = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 16)
        fpsClock = pygame.time.Clock()


    def renderMainMenuFrame(self, selItem):
        #self.screenSurface.blit()
        self.screenSurface.fill((4, 2, 12))
        self.screenSurface.fill((255, 255, 255), Rect(160, 50 * selItem + 200, 32, 32))
        pygame.display.update()
        fpsClock.tick(60)

    def renderHowToPlayFrame(self):
        bkgColor = pygame.Color(0, 0, 0)
        txtColor = pygame.Color(240, 240, 240)
        self.screenSurface.fill(bkgColor)
        self.font.render("How to play", True, txtColor)
        pygame.display.update()
        fpsClock.tick(60)

    def renderGameFrame(self):
        pygame.display.update()
        fpsClock.tick(60)

