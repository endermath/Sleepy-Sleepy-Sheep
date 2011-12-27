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
        self.speed = random.gauss(5, 2)

    def tick(self):
        pass


