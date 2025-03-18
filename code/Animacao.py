import pygame

from code.Const import SHIP_FRAMES


class animacao(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites_shot= []

        for i in range(len(SHIP_FRAMES)):
            self.sprites_shot.append(self.__get_sprite(i,SHIP_FRAMES[i]))

        # self.atual = 0
        # self.image = self.sprite_menu[self.atual]
        # self.rect = self.image.get_rect()
        # self.rect.topleft = 0, 0

    def __get_sprite(self, ship:int, frame: int):
        sprite = []
        for i in range(frame):
            self.name = f'ShotAnime-{ship}-{i}'
            sprite.append(pygame.image.load('asset/Sprites/' + self.name + '.png'))
        return sprite


    def update(self):
        self.atual = self.atual + 0.3
        if self.atual >= len(self.sprite_menu):
            self.atual = 0
        self.image = self.sprite_menu[int(self.atual)]