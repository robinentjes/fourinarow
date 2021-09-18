import pygame
from pygame import image as img
from button import Button
class MainMenuView:

    def __init__(self, screen, windowsize):
        self.screen = screen
        self.WINDOW_SIZE = windowsize
        self.background = img.load('images/mainMenuBackground.png')


    def display(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.background, (0,0))
        self.screen.blit(Button.oneVsOne, ((self.WINDOW_SIZE[0] / 2 - 200), 150))
        self.screen.blit(Button.oneVsAi, ((self.WINDOW_SIZE[0] / 2 - 200), 450))
