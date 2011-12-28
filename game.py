import random
from sheep import *

LEVEL_WHEN_BLACK_SHEEP_APPEAR = 5
LEVEL_WHEN_SHEEP_MOVING_BACKWARDS = 9
LEVEL_WHEN_PINK_SHEEP_APPEAR = 13

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
        self.sheepList = []
        self.gameClock = pygame.time.Clock()


    def newGame(self):
        self.level = 13

    def nextLevel(self):
        self.level += 1
        isTheLevelFinished = False
        self.whiteSheepCounter = 0
        self.blackSheepCounter = 0
        self.pinkSheepCounter = 0
        self.sheepTimer = 0
        self.nextSheep = 1000
        self.trollTimer = 0
        self.trollsAppeared = 0
        self.timeUntilTroll = random.gauss(1000 * 30.0 / self.level, 1000 * 10)

    def tick(self):
        msSinceLastTick = self.gameClock.tick()
        for sheep in self.sheepList:
            sheep.tick(msSinceLastTick)
            if sheep.relativePosx < -0.1:
                if sheep.cameFromTheRight:
                    self.correctSheepCount[sheep.color] += 1
                self.sheepList.remove(sheep)
#                print self.correctSheepCount
            elif sheep.relativePosx > 1.1:
                if not sheep.cameFromTheRight:
                    self.correctSheepCount[sheep.color] += 1
                self.sheepList.remove(sheep)
#                print self.correctSheepCount
        self.sheepTimer += msSinceLastTick
        self.trollTimer += msSinceLastTick

        if self.level >= LEVEL_WHEN_SHEEP_MOVING_BACKWARDS:
            startingDir = random.choice([SHEEP_MOVING_LEFT, SHEEP_MOVING_RIGHT])
        else:
            startingDir = SHEEP_MOVING_RIGHT
        if self.sheepTimer > self.nextSheep:
            if self.level >= LEVEL_WHEN_PINK_SHEEP_APPEAR:
                newSheep = Sheep(startingDir, random.choice([SHEEP_WHITE, SHEEP_BLACK, SHEEP_PINK]))
            elif self.level >= LEVEL_WHEN_BLACK_SHEEP_APPEAR:
                newSheep = Sheep(startingDir, random.choice([SHEEP_WHITE, SHEEP_BLACK]))
            else:
                newSheep = Sheep(startingDir, SHEEP_WHITE)
            self.sheepList.append(newSheep)
            self.sheepTimer = 0
            self.nextSheep = random.gauss(1000 * 4.0 / self.level, 500.0 / self.level)

        if self.trollsAppeared < self.level / 4 - 1:
            if self.trollTimer > self.timeUntilTroll:
                self.trollTimer = 0
                self.trollsAppeared += 1
                print "TROLOL"




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
