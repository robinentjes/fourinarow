import pygame
from pygame import image as img

class View:

    def __init__(self, width, height, margin, screen):
        # Define some colors
        pygame.font.init()
        self.font = pygame.font.Font('MAGNETOB.TTF', 60)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255,255,0)
        self.BLUE = (88, 114, 234)


        self.yellowBorder = img.load('images/yellowborder.png')
        self.redBorder = img.load('images/redborder.png')
        self.redBorderBackground = img.load('images/redborderbackground.png')
        self.greyBorderBackground = img.load('images/greybackground.png')
        self.yellowBorderBackground = img.load('images/yellowborderbackground.png')
        self.personIcon = img.load('images/personicon.png')
        self.robotIcon = img.load('images/roboticon.png')

        self.yellowCoin = img.load('images/yellowcoin.png')
        self.redCoin = img.load('images/redcoin.png')
        self.blackCoin = img.load('images/blackcoin.png')
        self.yellowCoinTrans = self.yellowCoin.copy()
        self.yellowCoinTrans.set_alpha(200)
        self.redCoinTrans = self.redCoin.copy()
        self.redCoinTrans.set_alpha(200)

        self.mainMenuButton = img.load('images/mainmenubutton.png')
        self.restartButton = img.load('images/restartbutton.png')

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = width
        self.HEIGHT = height
        # This sets the margin between each cell
        self.MARGIN = margin

        self.WINDOW_SIZE = [self.MARGIN * 8 + self.WIDTH * 7 + 500, self.MARGIN * 6 + self.HEIGHT * 6 + 150]
        self.screen = screen

        pygame.display.set_caption("Four in a row")
        self.clock = pygame.time.Clock()


    def drawGrid(self, board):
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen, self.BLUE, (
                0,
                130,
                ((self.MARGIN * 8) + (self.WIDTH * 7)),
                ((self.MARGIN * 7)) + (self.HEIGHT * 6)
        ))
        for row in range(6):
            for column in range(7):
                coin = self.blackCoin
                if board[row][column] == 1:
                    coin = self.yellowCoin
                elif board[row][column] == 2:
                    coin = self.redCoin

                self.screen.blit(coin, (((self.MARGIN + self.WIDTH) * column + self.MARGIN),
                                                        ((self.MARGIN + self.HEIGHT) * row) + 150))


    def hoverStone(self, currentPlayer, column):
        coin = self.yellowCoinTrans if currentPlayer == 1 else self.redCoinTrans
        self.screen.blit(coin, (((self.MARGIN + self.WIDTH) * column + self.MARGIN), 40))


    def drawPlayers(self, currentPlayer):
        if currentPlayer == 1:
            self.screen.blit(self.yellowBorderBackground, (745, 150))
            self.screen.blit(self.greyBorderBackground, (745, 300))
        else:
            self.screen.blit(self.greyBorderBackground, (745, 150))
            self.screen.blit(self.redBorderBackground, (745, 300))

        self.screen.blit(self.personIcon, (750,155))
        self.screen.blit(self.yellowBorder, (745, 150))
        playerName1 = self.font.render("Player 1", True, self.BLACK)
        self.screen.blit(playerName1, (870, 170))

        self.screen.blit(self.robotIcon, (750, 305))
        self.screen.blit(self.redBorder, (745, 300))
        playerName2 = self.font.render("Player 2", True, self.BLACK)
        self.screen.blit(playerName2, (870, 320))


    def drawButtons(self):
        self.screen.blit(self.restartButton, (753, 650))
        self.screen.blit(self.mainMenuButton, (986, 650))


    def quit(self):
        pygame.quit()
