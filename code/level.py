#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import event
from pygame.locals import QUIT

from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, mode ):
        self.window = window
        self.name = name
        self.mode = mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level'))
    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
            if event in pygame.event.get():
                if event.type == QUIT:

                    pass
        pass
