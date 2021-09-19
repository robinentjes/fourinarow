import pygame
from pygame import image as img
from button import Button

class GameDoneView:
    def __init__(self, screen):
        self.screen = screen

        self.personIcon = img.load('images/personicon.png')
        self.yellowBorder = img.load('images/yellowborder.png')
        self.yellowBorderBackground = img.load('images/yellowborderbackground.png')

        self.redBorderBackground = img.load('images/redborderbackground.png')
        self.redBorder = img.load('images/redborder.png')

        self.font = pygame.font.SysFont('monospace',  60)


    def display(self, winner):
        s = pygame.Surface((700,500), pygame.SRCALPHA)
        s.fill((255,255,255, 200))
        self.screen.blit(s, (260, 125))

        if winner == 1:
            text = self.font.render("Player 1 won!", False, (0,0,0))
            self.screen.blit(text, (380, 175))
        elif winner == -1:
            text = self.font.render("Player 2 won!", False, (0,0,0))
            self.screen.blit(text, (380, 175))
        else:
            text = self.font.render("Tie!", False, (0,0,0))
            self.screen.blit(text, (580, 175))

        self.screen.blit(Button.mainMenu, (360, 500))
        self.screen.blit(Button.restart, (660, 500))
