#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from pygame.locals import *
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.MenuAnimated import MenuAnimate

Animacao = pygame.sprite.Group()
AnimacaoMenu = MenuAnimate()
Animacao.add(AnimacaoMenu)


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Titulo_Game.png')
        self.rect = self.surf.get_rect(left=20, top=20)
    def run(self):
        pygame.mixer_music.load('./asset/cosmos.mp3')
        pygame.mixer.music.play(-1)
        while True:
            Animacao.draw(self.window)
            Animacao.update()
            self.menu_text(50,"New game 1P " ,(255,215,0),((WIN_WIDTH/2),300))
            self.menu_text(50, "New game 2P Coop ", (255, 215, 0), ((WIN_WIDTH / 2), 340))
            self.menu_text(50, "New game 2P Pvp ", (255, 215, 0), ((WIN_WIDTH / 2), 380))
            self.menu_text(50, "Score ", (255, 255, 255), ((WIN_WIDTH / 2), 420))
            pygame.display.flip()

            # checando todos os eventos
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()  # Fecha a janela do jogo
                    quit()  # Fecha o pygame
        pass

    def menu_text(self, text_size: int, text: str, color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size = text_size)
        text_surf: Surface = text_font.render(text,True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_position)
        self.window.blit(source=text_surf, dest=text_rect)

