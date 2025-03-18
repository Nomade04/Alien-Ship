#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.sprite = []
        self.atual = 0
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        if 'level' in name:
            self.surf = pygame.transform.scale(self.surf,(WIN_WIDTH,WIN_HEIGHT))
        if 'Enemy-1' in name:
            self.surf = pygame.transform.scale(self.surf,(80,45))
        elif 'Enemy' in name:
            self.surf = pygame.transform.scale(self.surf,(100,55))
        if 'Enemy-1Shot' in name:
            self.surf = pygame.transform.scale(self.surf,(20,10))
        elif 'Enemy-2Shot' in name:
            self.surf = pygame.transform.scale(self.surf,(35,30))
        elif 'Enemy-3Shot' in name:
            self.surf = pygame.transform.scale(self.surf, (50, 30))

        self.rect = self.surf.get_rect(left=position[0],top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
    @abstractmethod
    def move(self, ):
        pass
