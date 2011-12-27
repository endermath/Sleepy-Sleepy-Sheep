import random
from sheep import *

class Game(object):
    whiteSheepCounter = 0
    blackSheepCounter = 0
    pinkSheepCounter = 0
    correctSheepCount = [0, 0, 0]

    def __init__(self):
        self.isGameOver = False
        self.isTheLevelFinished = False
        self.level = 1
        sheepCenter = (200, 200)
        self.sheepList = [Sheep(SHEEP_MOVING_LEFT, random.choice([SHEEP_WHITE, SHEEP_BLACK, SHEEP_PINK]))]
        self.gameClock = pygame.time.Clock()
        self.gameCounter = 0

    def tick(self):
        msSinceLastTick = self.gameClock.tick()
        for sheep in self.sheepList:
            sheep.tick(msSinceLastTick)
            if sheep.relativePosx < -0.1:
                self.correctSheepCount[sheep.color] += 1
                self.sheepList.remove(sheep)
                print self.correctSheepCount
            elif sheep.relativePosx > 1.1:
                self.correctSheepCount[sheep.color] -= 1
                self.sheepList.remove(sheep)
                print self.correctSheepCount
        self.gameCounter += msSinceLastTick

        if self.gameCounter > 2000:
            self.sheepList.append(Sheep(SHEEP_MOVING_LEFT, random.choice([SHEEP_WHITE, SHEEP_BLACK, SHEEP_PINK])))
            self.gameCounter -= 2000





    def arrowButtonPressed(self, buttonId):
        # buttonId arrangement
        # 024
        # 135
        if buttonId == 0:
            self.whiteSheepCounter += 1
        elif buttonId == 1:
            self.whiteSheepCounter -= 1
        elif buttonId == 2:
            self.blackSheepCounter += 1
        elif buttonId == 3:
            self.blackSheepCounter -= 1
        elif buttonId == 4:
            self.pinkSheepCounter += 1
        elif buttonId == 5:
            self.pinkSheepCounter -= 1

    def newGame(self):
        self.level = 0

    def nextLevel(self):
        self.level += 1
        isTheLevelFinished = False
        self.whiteSheepCounter = 0
        self.blackSheepCounter = 0
        self.pinkSheepCounter = 0
