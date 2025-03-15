#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_type: str, postion=(0, 0)):
        match entity_type:
            case 'level':
                list_level = []
                for i in range(5):
                    list_level.append(Background(f'level_{i + 1}', (0, 0)))
                    list_level.append(Background(f'level_{i + 1}', (WIN_WIDTH, 0)))
                return list_level
            case 'Enemy-1':
                return Enemy('Enemy-1',(WIN_WIDTH +10, random.randint(50, WIN_HEIGHT - 80)))
            case 'Enemy-2':
                return Enemy('Enemy-2', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 80)))
            case 'Enemy-3':
                return Enemy('Enemy-3', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 80)))

