#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from code.menu import Menu


class Game:
    def __init__(self):
        pg.init()
        # Criando a janela do jogo com o parametro Tamanho
        self.window = pg.display.set_mode(size=(600, 480))

    def run(self):
        print("Setup start")
        print("Setup end")
        print("loop start")
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # checando todos os eventos
            # for event in pg.event.get():
            #     if event == pg.QUIT:
            #         pg.quit()  # Fecha a janela do jogo
            #         quit()  # Fecha o pygame

