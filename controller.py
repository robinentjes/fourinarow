from model import Board
from view import View
from mainmenuView import MainMenuView
from gameDoneView import GameDoneView
import pygame
import sys
import copy
import AIplayer

class Controller:

    def __init__(self, board):
        self.__board = board


        self.WIDTH = 80
        self.HEIGHT = 80
        # This sets the margin between each cell
        self.MARGIN = 20
        self.WINDOW_SIZE = [self.MARGIN * 8 + self.WIDTH * 7 + 500, self.MARGIN * 6 + self.HEIGHT * 6 + 150]
        print(self.WINDOW_SIZE)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.__view = View(self.WIDTH, self.HEIGHT, self.MARGIN, self.screen)
        self.__mainMenuView = MainMenuView(self.screen, self.WINDOW_SIZE)
        self.__gameDoneView = GameDoneView(self.screen)

        pygame.init()


    def mainMenuControl(self):
        self.__mainMenuView.display()
        pygame.display.flip()
        done = False

        while(not done):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    (x, y) = (position[0], position[1])
                    if x > 410 and x < 810 and y > 150 and y < 300:
                        self.gameControl("human")
                    if x > 410 and x < 810 and y > 450 and y < 600:
                        self.gameControl("ai")
            self.__mainMenuView.display()
            pygame.display.flip()


    def gameDoneController(self, winner):
        self.__view.drawGrid(self.__board.getBoard())
        self.__view.drawPlayers(winner)
        self.__view.drawButtons()
        self.__gameDoneView.display(winner)
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    (x, y) = (position[0], position[1])
                    if x > 360 and x < 560 and y > 500 and y < 570:
                        return "main"
                        done = True
                    elif x > 660 and x < 860 and y > 500 and y < 570:
                        self.__board.clearBoard()
                        return




    def gameControl(self, gameMode):
        currentPlayer = 1
        currentCol = 0
        self.__board.clearBoard()
        self.__view.drawGrid(self.__board.getBoard())

        done = False

        while(not done):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                position = pygame.mouse.get_pos()
                currentCol = position[0] // (self.__view.WIDTH + self.__view.MARGIN)
                currentCol = -1 if currentCol > 6 else currentCol

                if gameMode == "ai" and currentPlayer == -1:
                    move = AIplayer.decideMove(self.__board)
                    self.__board.addStone(-1, move)
                    if self.__board.isWin(-1, move):
                        ret = self.gameDoneController(-1)
                        if ret == "main":
                            return
                    currentPlayer = 1

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if currentCol != -1:
                        if not self.__board.canPlay(currentCol):
                            continue
                        self.__board.addStone(currentPlayer, currentCol)
                        checkWin = self.__board.isWin(currentPlayer, currentCol)
                        if checkWin:
                            ret = self.gameDoneController(currentPlayer)
                            if ret == "main":
                                return
                        else:
                            currentPlayer = - currentPlayer
                    else:
                        (x, y) = (position[0], position[1])
                        if x > 753 and x < 953 and y > 650 and y < 720:
                            self.__board.clearBoard()
                        elif x > 986 and x < 1186 and y > 650 and y < 720:
                            return


            self.__view.drawGrid(self.__board.getBoard())
            self.__view.drawPlayers(currentPlayer)
            self.__view.drawButtons()
            if currentCol != -1:
                self.__view.hoverStone(currentPlayer, currentCol)
            self.__view.clock.tick(60)
            pygame.display.flip()
