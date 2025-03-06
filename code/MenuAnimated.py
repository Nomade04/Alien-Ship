import pygame
from pygame.locals import *



class MenuAnimate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite_menu = []
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/MenuFrame1.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/MenuFrame2.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/MenuFrame3.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/MenuFrame4.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/MenuFrame5.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/MenuFrame6.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/MenuFrame7.png.png'))
        self.atual = 0
        self.image = self.sprite_menu[self.atual]
        self.rect = self.image.get_rect()
        self.rect,topleft = 0, 0

    def draw(self,window):
        self.window = window
        self.draw(self.window)

