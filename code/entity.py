#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import WIN_WIDTH, WIN_HEIGHT


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.sprite = []
        self.atual = 0
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        if 'level' in name:
            self.surf = pygame.transform.scale(self.surf,(WIN_WIDTH,WIN_HEIGHT))
        if 'Enemy-1' in name:
            self.surf = pygame.transform.scale(self.surf,(100,100))
        elif 'Enemy' in name:
            self.surf = pygame.transform.scale(self.surf,(150,150))

        self.rect = self.surf.get_rect(left=position[0],top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
