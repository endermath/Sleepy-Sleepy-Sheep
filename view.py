import pygame
from game import *
from icon import *

DARK_BLUE = pygame.Color(10, 10, 50)
CLOUD_COLOR = pygame.Color(240, 240, 240)

class View:
    def __init__(self, gam):
        self.game = gam
        self.fpsClock = pygame.time.Clock()
        pygame.display.set_caption("Sleepy Sleepy Sheep")
        self.screenSurface = pygame.display.set_mode((800, 600))

        self.menuFont = pygame.font.Font('Calligraffiti.ttf', 34)
        self.sheepCounterFont = pygame.font.Font('Calligraffiti.ttf', 22)
        self.sheepCounterFont.set_bold(True)  #'u'/Library/Fonts/Zapfino.ttf', 22)

        self.featherSurf = pygame.image.load('feather.png')

        self.cloudSurf = pygame.image.load('bigcloud.png')
        self.cloudRect = self.screenSurface.get_rect()
        self.cloudRect.height = self.cloudRect.height * 3 / 4

        self.buttonUpSurf = pygame.image.load('arrowbutton.png')
        self.buttonDownSurf = pygame.transform.flip(self.buttonUpSurf, False, True)

        self.wallSurf = pygame.image.load('wall.png')
        self.wallRect = self.wallSurf.get_rect()
        self.wallRect.midbottom = self.cloudRect.move(0, -self.cloudSurf.get_rect().height).midbottom

        self.sheepSurfaceSheet = pygame.image.load("sheep2.png")
        self.sheepSurfList = [[self.sheepSurfaceSheet.subsurface(pygame.Rect(128 * j, 64 * i, 128, 64))   for j in range(3)]  for i in range(4)]


        self.whiteSheepSurface1 = self.sheepSurfaceSheet.subsurface(pygame.Rect(0, 128, 128, 64))
        #self.whiteSheepSurface2 = self.sheepSurfaceSheet.subsurface(pygame.Rect(0, 64, 128, 64))
        self.blackSheepSurface1 = self.sheepSurfaceSheet.subsurface(pygame.Rect(128, 128, 128, 64))
        #self.blackSheepSurface2 = self.sheepSurfaceSheet.subsurface(pygame.Rect(128, 64, 128, 64))
        self.pinkSheepSurface1 = self.sheepSurfaceSheet.subsurface(pygame.Rect(256, 128, 128, 64))
        #self.pinkSheepSurface2 = self.sheepSurfaceSheet.subsurface(pygame.Rect(256, 64, 128, 64))

        self.sheepIcons = []
        self.buttonIcons = []


    def renderMainMenuFrame(self, selItem):
        bkgColor = DARK_BLUE
        txtColor = pygame.Color(240, 240, 240)
        self.screenSurface.fill(bkgColor)
        txtList = [self.menuFont.render(txt, True, txtColor) for txt in ["Sleepy sleepy sheep",
                                                               "Go to bed",
                                                               "Instructions",
                                                               "Quit"]]
        rect = [txt.get_rect() for txt in txtList]
        srect = self.screenSurface.get_rect()
        rect[0].centerx = srect.centerx
        rect[0].centery = srect.centery - 200
        rect[1].centerx = srect.centerx
        rect[1].centery = rect[0].centery + 180
        rect[2].centerx = srect.centerx
        rect[2].centery = rect[1].centery + 80
        rect[3].centerx = srect.centerx
        rect[3].centery = rect[2].centery + 80

        for i in range(4):
            self.screenSurface.blit(txtList[i], rect[i])

        featherRect = self.featherSurf.get_rect()
        featherRect.centerx = rect[2].move(-featherRect.width, 0).left
        featherRect.centery = rect[1 + selItem].centery
        self.screenSurface.blit(self.featherSurf, featherRect)

        pygame.display.update()
        self.fpsClock.tick(60)

    def renderHowToPlayFrame(self):
        self.screenSurface.fill(DARK_BLUE)
        txtColor = pygame.Color(240, 240, 240)
        txt1 = self.menuFont.render("How to play", True, txtColor)
        rect1 = txt1.get_rect().move(self.screenSurface.get_rect().center)
        self.screenSurface.blit(txt1, rect1)
        pygame.display.update()
        self.fpsClock.tick(60)

    def nextLevel(self):
        # Setup icons
        if self.game.level < LEVEL_WHEN_BLACK_SHEEP_APPEAR:
            sheepIconRect0 = self.whiteSheepSurface1.get_rect()
            sheepIconRect0.center = (self.screenSurface.get_rect().centerx,
                                    self.screenSurface.get_rect().height / 5)
            self.sheepIcons = [Icon(self.whiteSheepSurface1, sheepIconRect0)]
        elif self.game.level < LEVEL_WHEN_PINK_SHEEP_APPEAR:
            sheepIconRect0 = self.whiteSheepSurface1.get_rect()
            sheepIconRect0.center = (self.screenSurface.get_rect().centerx - sheepIconRect0.width ,
                                    self.screenSurface.get_rect().height / 5)

            sheepIconRect1 = self.blackSheepSurface1.get_rect()
            sheepIconRect1.center = (self.screenSurface.get_rect().centerx + sheepIconRect1.width,
                                    self.screenSurface.get_rect().height / 5)
            self.sheepIcons = [Icon(self.whiteSheepSurface1, sheepIconRect0), Icon(self.blackSheepSurface1, sheepIconRect1)]
        else:
            sheepIconRect0 = self.whiteSheepSurface1.get_rect()
            sheepIconRect0.center = (self.screenSurface.get_rect().centerx - sheepIconRect0.width * 2,
                                    self.screenSurface.get_rect().height / 5)

            sheepIconRect1 = self.blackSheepSurface1.get_rect()
            sheepIconRect1.center = (self.screenSurface.get_rect().centerx,
                                    self.screenSurface.get_rect().height / 5)

            sheepIconRect2 = self.pinkSheepSurface1.get_rect()
            sheepIconRect2.center = (self.screenSurface.get_rect().centerx + sheepIconRect2.width * 2,
                                    self.screenSurface.get_rect().height / 5)
            self.sheepIcons = [Icon(self.whiteSheepSurface1, sheepIconRect0),
                               Icon(self.blackSheepSurface1, sheepIconRect1),
                               Icon(self.pinkSheepSurface1, sheepIconRect2)]

            # Setup button icons
            #buttonUpRect = self.buttonUpSurf.get_rect()
            #buttonUpRect.midbottom = self.sheepIcons[0].rect.midtop

            #buttonDownRect = self.buttonDownSurf.get_rect()
            #buttonDownRect.midtop = self.sheepIcons[0].rect.midbottom

            #self.buttonIcons = [Icon(self.buttonUpSurf, buttonUpRect), Icon(self.buttonDownSurf, buttonDownRect)]

    def renderGameFrame(self):
        self.screenSurface.fill(DARK_BLUE)

        # Render cloud
        self.screenSurface.fill(CLOUD_COLOR, self.cloudRect)
        xpos = 0
        while xpos < self.cloudRect.width:
            self.screenSurface.blit(pygame.transform.flip(self.cloudSurf, False, True), (xpos, self.cloudRect.top))
            self.screenSurface.blit(self.cloudSurf, (xpos, self.cloudRect.bottom - self.cloudSurf.get_rect().height))
            xpos += self.cloudSurf.get_rect().width

        # Render buttons and icons
        #for button in self.buttonIcons:
        #    self.screenSurface.blit(button.surf, button.rect)
        for sheep in self.sheepIcons:
            self.screenSurface.blit(sheep.surf, sheep.rect)

        if self.game.level >= LEVEL_WHEN_PINK_SHEEP_APPEAR:
            sheepNumber = self.sheepCounterFont.render(str(self.game.correctSheepCount[2]), True, (20, 60, 20))
            sheepNumberRect = sheepNumber.get_rect()
            sheepNumberRect.center = self.sheepIcons[2].rect.center
            self.screenSurface.blit(sheepNumber, sheepNumberRect)
        if self.game.level >= LEVEL_WHEN_BLACK_SHEEP_APPEAR:
            sheepNumber = self.sheepCounterFont.render(str(self.game.correctSheepCount[1]), True, (20, 60, 20))
            sheepNumberRect = sheepNumber.get_rect()
            sheepNumberRect.center = self.sheepIcons[1].rect.center
            self.screenSurface.blit(sheepNumber, sheepNumberRect)

        sheepNumber = self.sheepCounterFont.render(str(self.game.correctSheepCount[0]), True, (20, 60, 20))
        sheepNumberRect = sheepNumber.get_rect()
        sheepNumberRect.center = self.sheepIcons[0].rect.center
        self.screenSurface.blit(sheepNumber, sheepNumberRect)


        # Render the wall
        self.screenSurface.blit(self.wallSurf, self.wallRect)

        # Render all the moving sheep
        for sheep in self.game.sheepList:
            scrSize = self.screenSurface.get_rect().size
            sheepSurf = self.sheepSurfList[sheep.frame][sheep.color]
            if sheep.dir == SHEEP_MOVING_RIGHT:
                sheepSurf = pygame.transform.flip(sheepSurf, True, False)
            sw = sheepSurf.get_rect().width
            sheepPos = (sheep.relativePosx * (scrSize[0] + sw) - sw , sheep.relativePosy * scrSize[1])
            sheepRect = pygame.Rect(sheepPos, sheepSurf.get_rect().size)
            self.screenSurface.blit(sheepSurf, sheepPos)

            sheepHeadRect = sheepRect.inflate(-100, -20).move(sheep.dir * 50, 0)
            sheepFeetRect = sheepRect.inflate(-40, -40).move(0 , 20)
            #pygame.draw.rect(self.screenSurface, (0, 0, 0), sheepHeadRect, 2)
            #pygame.draw.rect(self.screenSurface, (0, 0, 0), sheepFeetRect, 2)
            if sheepHeadRect.colliderect(self.wallRect.inflate(-20, -20)):
                sheep.bumpHead()
            if sheepFeetRect.colliderect(self.wallRect.inflate(-20, -20)):
                sheep.bumpFeet()

        pygame.display.update()
        self.fpsClock.tick(60)

    def showLevelResults(self):
        pass
