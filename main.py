#!/usr/bin/python

# Libs
import pygame
import sys
from pygame.locals import *

# My files
from game import *
from view import *

def main():

    # Basic pyGame setup
    pygame.init()

    # Create 
    game = Game()
    view = View(game)

    hasChosenToQuit = False
    while not hasChosenToQuit:
        isInMainMenu = True
        selectedItem = 0            # 0=Play, 1=How to play, 2=Quit
        while isInMainMenu:
            view.renderMainMenuFrame(selectedItem)
            for event in pygame.event.get():
                if event.type == QUIT:
                    selectedItem = 2
                    isInMainMenu = False
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        isInMainMenu = False
                    elif event.key == K_DOWN:
                        selectedItem = min(selectedItem + 1, 2)
                    elif event.key == K_UP:
                        selectedItem = max(selectedItem - 1, 0)

        if selectedItem == 0:
            # Create new game
            game.newGame()
            while not game.isGameOver:
                game.nextLevel()
                isTheLevelFinished = False
                while not isTheLevelFinished:

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            #left mouse button clicked
                            mousePos = pygame.mouse.get_pos()

                    view.renderGameFrame()
                gameOver = game.showLevelResults()

        elif selectedItem == 1:
            print "how to play"
            waitingForSpace = True
            while waitingForSpace:
                view.renderHowToPlayFrame()
                for event in pygame.event.get():
                    if event.type == KEYDOWN and event.key == K_SPACE:
                        waitingForSpace = False

        elif selectedItem == 2:
            hasChosenToQuit = True

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
