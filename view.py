import pygame
from game import *

class View:
    def __init__(self, gam):
        self.game = gam
        pygame.display.set_caption("Sleepy Sleepy Sheep")
        self.screenSurface = pygame.display.set_mode((800, 600))
        fontname = pygame.font.match_font('Zapfino')
        print fontname
        self.font = pygame.font.Font(u'/Library/Fonts/Zapfino.ttf', 34)
        self.fpsClock = pygame.time.Clock()


    def renderMainMenuFrame(self, selItem):
        bkgColor = pygame.Color(10, 10, 20)
        txtColor = pygame.Color(240, 240, 240)
        self.screenSurface.fill(bkgColor)
        txt1 = self.font.render("Sleepy sleepy sheep", True, txtColor)
        txt2 = self.font.render("Go to bed", True, txtColor)
        txt3 = self.font.render("Instructions", True, txtColor)
        txt4 = self.font.render("Quit", True, txtColor)
        rect1 = txt1.get_rect()
        rect1.centerx = self.screenSurface.get_rect().centerx
        rect1.centery = self.screenSurface.get_rect().centery - 100
        rect2 = rect1.move(0, 80)
        rect3 = rect2.move(0, 80)
        rect4 = rect3.move(0, 80)
        self.screenSurface.blit(txt1, rect1)
        self.screenSurface.blit(txt2, rect2)
        self.screenSurface.blit(txt3, rect3)
        self.screenSurface.blit(txt4, rect4)

        rect5 = rect2.move(-50, 40 + 80 * selItem)
        rect5.size = (20, 20)
        self.screenSurface.fill((255, 255, 255), rect5)
        pygame.display.update()
        self.fpsClock.tick(60)

    def renderHowToPlayFrame(self):
        bkgColor = pygame.Color(0, 0, 0)
        txtColor = pygame.Color(240, 240, 240)
        self.screenSurface.fill(bkgColor)
        txt1 = self.font.render("How to play", True, txtColor)
        rect1 = txt1.get_rect().move(self.screenSurface.get_rect().center)
        self.screenSurface.blit(txt1, rect1)
        pygame.display.update()
        self.fpsClock.tick(60)

    def renderGameFrame(self):
        pygame.display.update()
        self.fpsClock.tick(60)

    def showLevelResults(self):
        pass
