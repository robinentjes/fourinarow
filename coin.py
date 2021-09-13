import pygame
from pygame import image as img

class Coin:
    yellow = img.load('images/greencoin.png')
    red = img.load('images/purplecoin.png')
    black = img.load('images/blackcoin.png')
    yellowTrans = yellow.copy()
    yellowTrans.set_alpha(200)
    redTrans = red.copy()
    redTrans.set_alpha(200)
