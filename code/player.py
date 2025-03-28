#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_HEIGHT
from code.PlayerShot import PlayerShot


class Player(pygame.sprite.Sprite):
    def __init__(self, number: int):
        super().__init__()
        self.instancing = False
        self.sprite = []
        self.atual = 0
        self.number = number
        self.shot_delay = 5
        self.health = 5
        self.instance = True
        self.respaw_health = 5
        self.rect_heart_leaft = 80
        self.rect_heart_top = 15
        self.heart = pygame.image.load('asset/heart.png')

        if number == 1:
            for i in range(10):
                self.name = f'Player1_{i + 1}'
                self.img = pygame.image.load('asset/' + self.name + '.png')
                self.img = pygame.transform.scale(self.img, (100, 100))
                self.sprite.append(self.img)
                self.rect_heart_leaft = 80
                self.rect_heart_top = 15
        elif number == 2:
            for i in range(10):
                self.name = f'Player2-{i + 1}'
                self.img = pygame.image.load('asset/' + self.name + '.png.png')
                self.img = pygame.transform.scale(self.img, (100, 100))
                self.sprite.append(self.img)
                self.rect_heart_leaft = 270
                self.rect_heart_top = 15

        self.image = self.sprite[self.atual]
        self.rect = self.image.get_rect()
        if number == 1:
            self.rect.topleft = 10, WIN_HEIGHT / 2
            self.respaw_point = 10, WIN_HEIGHT / 3
            self.HudPicture = pygame.image.load('asset/Player1-Picture.png').convert_alpha()
            self.img = pygame.transform.scale(self.HudPicture, (100, 100))
            self.HudRect = self.HudPicture.get_rect(left=10, top=10)

        elif number == 2:
            self.rect.topleft = 10, WIN_HEIGHT / 5
            self.respaw_point = self.rect.topleft
            self.HudPicture = pygame.image.load('asset/Player2-Picture.png')
            self.img = pygame.transform.scale(self.HudPicture, (100, 100))
            self.HudRect = self.HudPicture.get_rect(left=200, top=10)


    def move(self, number: int):
        if number == 1:
            pressed_k = pygame.key.get_pressed()
            if self.instance:
                if not self.rect.centerx <= 50:
                    if pressed_k[pygame.K_a]:
                        self.rect.centerx -= 1
                if not self.rect.centerx >= 400:
                    if pressed_k[pygame.K_d]:
                        self.rect.centerx += 1
                if not self.rect.centery >= WIN_HEIGHT - 50:
                    if pressed_k[pygame.K_s]:
                        self.rect.centery += 1
                if not self.rect.centery <= 50:
                    if pressed_k[pygame.K_w]:
                        self.rect.centery -= 1
        elif number == 2:
            pressed_k = pygame.key.get_pressed()
            if self.instance:
                if not self.rect.centerx <= 50:
                    if pressed_k[pygame.K_LEFT]:
                        self.rect.centerx -= 1
                if not self.rect.centerx >= 400:
                    if pressed_k[pygame.K_RIGHT]:
                        self.rect.centerx += 1
                if not self.rect.centery >= WIN_HEIGHT - 50:
                    if pressed_k[pygame.K_DOWN]:
                        self.rect.centery += 1
                if not self.rect.centery <= 50:
                    if pressed_k[pygame.K_UP]:
                        self.rect.centery -= 1

    def shot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = 10
            return PlayerShot(name='Player-Shot', position = (self.rect.centerx,self.rect.centery +30))


    def HubHeart(self, window):
        rect_heart_leaft = self.rect_heart_leaft
        for i in range(self.health):
            window.blit(source=self.heart, dest=(rect_heart_leaft,self.rect_heart_top))
            rect_heart_leaft+= 20


    def update(self):
        self.atual = self.atual + 0.04
        if self.atual >= len(self.sprite):
            self.atual = 0
        self.image = self.sprite[int(self.atual)]
