import pygame
import random

SHEEP_WHITE = 0
SHEEP_BLACK = 1
SHEEP_PINK = 2

SHEEP_MOVING_LEFT = -1
SHEEP_MOVING_RIGHT = 1



class Sheep(object):
    def __init__(self, dir=SHEEP_MOVING_LEFT, color=SHEEP_WHITE):
        # Set direction, and speed of movement.
        self.dir = dir
        self.color = color
        self.speedy = 0
        self.speedx = random.gauss(0.20, 0.04)        #speed in screens/second (e.g. 800px/secons)
        self.relativePosy = 0.5
        if self.dir == SHEEP_MOVING_LEFT:
            self.relativePosx = 1
        else:
            self.relativePosx = 0
        self._counter = 0
        self.frame = 0

        # Sound effects
        self.sheepJumpSound = pygame.mixer.Sound('sheepjump.wav')


    def tick(self, msSinceLastTick):
        self._counter = (self._counter + msSinceLastTick) % 1000
        # if in the air
        if self.relativePosy < 0.5:
            self.frame = 1
            self.speedy += 0.5 * msSinceLastTick / 1000.0
        else:
            self.frame = 2 + self._counter / 500

        self.relativePosx += self.dir * self.speedx * msSinceLastTick / 1000.0
        self.relativePosy += self.speedy * msSinceLastTick / 1000.0
        if self.relativePosy > 0.5 and self.speedy > 0:
            self.relativePosy = 0.5
            self.speedy = 0

        if self.relativePosx < 0.65 and self.relativePosx > 0.55 and self.relativePosy == 0.5:
            self.speedy = -random.gauss(0.40, 0.06)
            self.sheepJumpSound.play()







