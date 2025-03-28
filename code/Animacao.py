# import pygame
#
# from code.Const import SHIP_FRAMES, ANIMATED_TIME, SHOT_DELAY, ANIM_DELAY, ENTITY_SPEED
#
#
# class animacao():#pygame.sprite.Sprite
#
#     def __init__(self, ship):
#         super().__init__()
#         self.sprite = []
#         self.atual = 0
#         for i in range(SHIP_FRAMES[ship]):  # len(SHIP_FRAMES)
#             self.name = f'ShotAnime-{ship}-{i + 1}'
#             self.surf = pygame.image.load('asset/Sprites/' + self.name + '.png')
#             self.surf = pygame.transform.scale(self.surf, (40, 10))
#             self.sprite.append(self.surf)
#         self.image = self.sprite[self.atual]
#         self.rect = self.image.get_rect()
#         self.now = 0
#         self.finished = False  # Adicionado para controlar se a animação terminou
#
#         # self.rect.topleft =ent[0]-50,ent[1]
#
#     def move(self):
#         self.rect.centerx -= 1#ENTITY_SPEED[f'Enemy-{ship}']
#     def update(self):
#         if not self.finished:
#             for i in range(4):# Só atualizar se a animação não estiver concluída
#                 self.atual += 1
#                 if self.atual >= len(self.sprite):  # Se passar do último frame
#                     self.finished = True
#                     # Marcar a animação como concluída
#                 else:
#                     self.image = self.sprite[self.atual]