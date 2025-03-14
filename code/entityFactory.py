#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH
from code.background import Background


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


