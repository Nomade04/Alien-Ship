import pygame

class MenuAnimate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sprite_menu = []
        for i in range(8):
            self.name = f'Menu_Select-{i + 1}'
            self.sprite_menu.append(pygame.image.load('asset/MenuFrame/' + self.name + '.png.png'))

        self.atual = 0
        self.image = self.sprite_menu[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0

    def update(self):
        self.atual = self.atual + 0.3
        if self.atual >= len(self.sprite_menu):
            self.atual = 0
        self.image = self.sprite_menu[int(self.atual)]




