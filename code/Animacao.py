import pygame

from code.Const import SHIP_FRAMES, ANIMATED_TIME


class animacao(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites_shot= []
        for i in range(len(SHIP_FRAMES)):
            self.sprites_shot.append(self.__get_sprite(i,SHIP_FRAMES[i]))



    def animated(self, ship, position):
        self.atual = 0
        self.image = self.sprites_shot[ship[self.atual]]
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        return self.__update(ship,ANIMATED_TIME[ship],SHIP_FRAMES[ship])

    def __get_sprite(self, ship:int, frame: int):
        sprite = []
        for i in range(frame):
            self.name = f'ShotAnime-{ship}-{i}'
            sprite.append(pygame.image.load('asset/Sprites/' + self.name + '.png'))
        return sprite


    def __update(self,ship, AnimatedTime, frame):
        for i in range(AnimatedTime):
            self.atual = self.atual + (frame/AnimatedTime)
            if self.atual >= len(self.sprites_shot[ship]):
                self.atual = 0
        self.image = self.sprites_shot[ship[int(self.atual)]]