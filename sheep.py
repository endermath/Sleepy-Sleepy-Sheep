import pygame
import random

SHEEP_WHITE = 0
SHEEP_BLACK = 1
SHEEP_PINK = 2

SHEEP_MOVING_LEFT = -1
SHEEP_MOVING_RIGHT = 1

sheepSurfaceSheet = pygame.image.load("sheep.png")

whiteSheepSurface1 = sheepSurfaceSheet.subsurface(pygame.Rect(0,0,128,64))
whiteSheepSurface2 = sheepSurfaceSheet.subsurface(pygame.Rect(0,64,128,64))
blackSheepSurface1 = sheepSurfaceSheet.subsurface(pygame.Rect(128,0,128,64))
blackSheepSurface2 = sheepSurfaceSheet.subsurface(pygame.Rect(128,64,128,64))
pinkSheepSurface1 = sheepSurfaceSheet.subsurface(pygame.Rect(256,0,128,64))
pinkSheepSurface2 = sheepSurfaceSheet.subsurface(pygame.Rect(256,64,128,64))


class Sheep(object):
    def __init__(self, dir = SHEEP_MOVING_LEFT):
        # Call super's (=Rect's) __init__. This defines Sheep when viewed as a Rect.
        self.rect = pygame.Rect(0,0,128,64)
        self.surf1 = whiteSheepSurface1
        self.surf2 = whiteSheepSurface2
        # Set direction, and speed of movement.
        self.dir = dir
        self.speed = random.gauss(5,2)

        # Initialize animation counter
        self._animation_counter = 0

    def tick(self):
        self._animation_counter = (self._animation_counter + 1) % 10*FPS
        
        
    def render(self,scrSurf):
        if self._animation_counter % 2*FPS > FPS:
            surf = self.surf1
        else:
            surf = self.surf2
        
        scrSurf.blit(surf,self.rect)
        
        

class WhiteSheep(Sheep):
    def __init__(self, center, dir = SHEEP_MOVING_LEFT):
        Sheep.__init__(self,dir)
        self.surf1 = whiteSheepSurface1
        self.surf2 = whiteSheepSurface2

class BlackSheep(Sheep):
    def __init__(self, center, dir = SHEEP_MOVING_LEFT):
        Sheep.__init__(self,dir)
        self.surf1 = blackSheepSurface1
        self.surf2 = blackSheepSurface2

class PinkSheep(Sheep):
    def __init__(self, center, dir = SHEEP_MOVING_LEFT):
        Sheep.__init__(self,dir)
        self.surf1 = pinkSheepSurface1
        self.surf2 = pinkSheepSurface2




