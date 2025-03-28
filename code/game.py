#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, text
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        # Criando a janela do jogo com o parametro Tamanho
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [text[0],text[1],text[2]]:
                level = Level(self.window,'Level 1', menu_return)
                level_return = level.run()
                if level_return:
                    level_return = Level(self.window,'Level 2', menu_return).run()
                    if level_return:
                        level_return = Level(self.window,'Level 3', menu_return).run()
                        if level_return:
                            pass



