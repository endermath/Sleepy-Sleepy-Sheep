import pygame,random
from general import FPS

SHEEP_WHITE = 0
SHEEP_BLACK = 1
SHEEP_PINK = 2

SHEEP_MOVING_LEFT = -1
SHEEP_MOVING_RIGHT = 1

sheepSurfaceSheet = pygame.image.load("sheep.png")

whiteSheepSurface1 = sheepSurfaceSheet.subsurface(Rect(0,0,128,64))
whiteSheepSurface2 = sheepSurfaceSheet.subsurface(Rect(0,64,128,64))
blackSheepSurface1 = sheepSurfaceSheet.subsurface(Rect(128,0,128,64))
blackSheepSurface2 = sheepSurfaceSheet.subsurface(Rect(128,64,128,64))
pinkSheepSurface1 = sheepSurfaceSheet.subsurface(Rect(256,0,128,64))
pinkSheepSurface2 = sheepSurfaceSheet.subsurface(Rect(256,64,128,64))


def class Sheep(pygame.Rect):
    def __init__(self, dir = SHEEP_MOVING_LEFT)
        # Call super's (=Rect's) __init__. This defines Sheep when viewed as a Rect.
        super(Sheep,self).__init__(0,0,128,64)
        self.surf1 = None
        self.surf2 = None
        # Set direction, and speed of movement.
        self.dir = dir
        self.speed = random.gauss(5,2)

        # Initialize animation counter
        self.animationCounter = 0
    def tick(self):
        self.animationCounter += 1
        
    def render(self,screenSurf):
        if animationCounter > FPS/2:
            screenSurf.blit(surf1
        

def class WhiteSheep(Sheep):
    def __init__(self, center, dir = SHEEP_MOVING_LEFT):
        super(WhiteSheep,self).__init__(dir)
        self.surf1 = whiteSheepSurface1
        self.surf2 = whiteSheepSurface2

def class BlackSheep(Sheep):
    def __init__(self, center, dir = SHEEP_MOVING_LEFT):
        super(BlackSheep,self).__init__(dir)
        self.surf1 = blackSheepSurface1
        self.surf2 = blackSheepSurface2

def class WhiteSheep(Sheep):
    def __init__(self, center, dir = SHEEP_MOVING_LEFT):
        super(PinkSheep,self).__init__(dir)
        self.surf1 = pinkSheepSurface1
        self.surf2 = pinkSheepSurface2




