import pygame

from code.Const import SHIP_FRAMES, ANIMATED_TIME, SHOT_DELAY, ANIM_DELAY


class animacao(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprite= []








    def animated(self, ship):
        for i in range(SHIP_FRAMES[ship]):  # len(SHIP_FRAMES)
            self.name = f'ShotAnime-{ship}-{i + 1}'
            self.surf = pygame.image.load('asset/Sprites/' + self.name + '.png')
            self.surf = pygame.transform.scale(self.surf, (80, 45))
            self.sprite.append(self.surf)
            return self.sprite


    # def __get_sprite(self, ship:int, frame: int):
    #     sprite = []
    #     for i in range(frame):
    #         self.name = f'ShotAnime-{ship + 1}-{i+1}'
    #         surf = pygame.image.load('asset/Sprites/' + self.name + '.png')
    #         self.surf = pygame.transform.scale(surf,(80,45))
    #         sprite.append(surf)


        # return sprite

        return True
    def update(self):

            self.atual = self.atual + 0.5#(frame/AnimatedTime)
            if self.atual >= len(self.sprite):
                self.atual = 0
            self.image = self.sprite[int(self.atual)]