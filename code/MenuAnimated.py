import pygame
from pygame.locals import *



class MenuAnimate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite_menu = []
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/Menu_Select-1.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/Menu_Select-2.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/Menu_Select-3.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/Menu_Select-4.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/Menu_Select-5.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/Menu_Select-6.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/Menu_Select-7.png.png'))
        self.sprite_menu.append(pygame.image.load('asset/MenuFrame/Menu_Select-8.png.png'))
        self.atual = 0
        self.image = self.sprite_menu[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0

    def update(self):
        self.atual = self.atual + 0.3
        if self.atual >= len(self.sprite_menu):
            self.atual = 0
        self.image = self.sprite_menu[int(self.atual)]




