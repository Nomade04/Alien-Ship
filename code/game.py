#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        # Criando a janela do jogo com o parametro Tamanho
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        print("Setup start")
        print("Setup end")
        print("loop start")

        while True:
            menu = Menu(self.window)
            menu.run()
            pass



