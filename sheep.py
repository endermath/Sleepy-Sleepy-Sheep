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
        self.speed = random.gauss(0.10, 0.02)        #speed in screens/second (e.g. 800px/secons)
        self.relativePosy = 0.5
        if self.dir == SHEEP_MOVING_LEFT:
            self.relativePosx = 1
        else:
            self.relativePosx = 0
        self._counter = 0
        self.frame = 0

    def tick(self, msSinceLastTick):
        self._counter += msSinceLastTick
        while self._counter > 500:
            self.frame = 1 - self.frame
            self._counter -= 500

        self.relativePosx += self.dir * msSinceLastTick * self.speed / 1000.0






