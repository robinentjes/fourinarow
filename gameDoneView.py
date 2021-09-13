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


    def display(self, winner):
        pygame.draw.rect(self.screen, (150,150,200), (260, 125, 700, 500))

        if winner == 1:
            self.screen.blit(self.yellowBorderBackground, (410, 175))
            self.screen.blit(self.personIcon, (415,180))
            self.screen.blit(self.yellowBorder, (410, 175))
        else:
            self.screen.blit(self.redBorderBackground, (410, 175))
            self.screen.blit(self.personIcon, (415,180))
            self.screen.blit(self.redBorder, (410, 175))

        self.screen.blit(Button.mainMenu, (360, 500))
        self.screen.blit(Button.restart, (660, 500))
