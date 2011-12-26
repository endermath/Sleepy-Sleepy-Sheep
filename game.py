import random
from sheep import *
from player import *
from arrowbutton import *

class Game(object):

    def __init__(self):
        self.isGameOver = False
        self.level = 1
        sheepCenter = (200, 200)
        self.sheepList = [random.choice([WhiteSheep(sheepCenter), BlackSheep(sheepCenter), PinkSheep(sheepCenter)])]

    def tick(self):
        playingLevel = True

    def render(self, scrSurf):
        for sheep in self.sheepList:
            sheep.render(scrSurf)

    def newGame(self):
        pass

    def nextLevel(self):
        pass

    def showLevelResults(self):
        return True
