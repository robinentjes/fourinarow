import pygame
from pygame import image as img
class MainMenuView:

    def __init__(self, screen, windowsize):
        self.screen = screen
        self.WINDOW_SIZE = windowsize

        self.oneVsOne = img.load('images/onevone.png')
        self.oneVsAi = img.load('images/onevAI.png')


    def display(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.oneVsOne, ((self.WINDOW_SIZE[0] / 2 - 200), 150))
        self.screen.blit(self.oneVsAi, ((self.WINDOW_SIZE[0] / 2 - 200), 450))
