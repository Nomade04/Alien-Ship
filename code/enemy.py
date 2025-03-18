#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_WIDTH, SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = SHOT_DELAY[self.name]

            if self.name == 'Enemy-1':
                return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx -70, self.rect.centery -5))

            elif self.name == 'Enemy-2':
                return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx - 70, self.rect.centery - 14))

            elif self.name == 'Enemy-3':
                return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx - 85, self.rect.centery - 5))






