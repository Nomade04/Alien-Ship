#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from pygame.locals import *
from code.Const import *
from code.MenuAnimated import MenuAnimate

# Instanciando Fundo animado do menu
Animacao = pygame.sprite.Group()
AnimacaoMenu = MenuAnimate()
Animacao.add(AnimacaoMenu)


class Menu:
    def __init__(self, window):
        self.window = window

        # Criando titulo do game
        self.title = pygame.image.load('./asset/MenuFrame/Titulo_Game.png')
        self.rect = self.title.get_rect(left=(WIN_WIDTH / 4), top=75)
        self.title = pygame.transform.scale(self.title, (655 / 1.5, 211 / 1.5))

        # Atributos de iteração
        self.op_atual = 0
        self.op_exitAtual = None
        self.Exit = None
        self.close = None

        # Mensagen de saida
        self.exit_scren = pygame.image.load('./asset/MenuFrame/EXIT_scren.png')
        self.exit_rect = self.exit_scren.get_rect(left=(150), top=60)
        self.exit_scren = pygame.transform.scale(self.exit_scren, (510, 400))

    def run(self):
        pygame.mixer_music.load('./asset/Sounds/cosmos.mp3')
        pygame.mixer.music.play(-1)

        while True:
            # Colocando animação de fundo e titulo
            Animacao.draw(self.window)
            Animacao.update()
            self.window.blit(source=self.title, dest=self.rect)

            # Mensagem de saida e fechamendo pelo menu
            if self.Exit:
                self.window.blit(exit_scren,exit_rect)
                self.menu_text(40, 'Are you sure you want to leave?', COLOR_WHITE, ((WIN_WIDTH / 2), 205))
                self.select_exit(self.op_exitAtual, exit_listPosition, exit_listText)
                if self.close:
                    pygame.quit()  # Fecha a janela do jogo
                    quit()
            else:
                self.select(self.op_atual, select_list, text)

            pygame.display.flip()

            # checando todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Exit = True  # Fecha o pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        if self.op_atual == 4:
                            self.op_atual = 0
                        else:
                            self.op_atual += 1
                    if event.key == pygame.K_w:
                        if self.op_atual == 0:
                            self.op_atual = 4
                        else:
                            self.op_atual += -1
                    if event.key == pygame.K_a:
                        self.op_atual = 4
                        if self.Exit:
                            if self.op_exitAtual == 0:
                                self.op_exitAtual = 1
                            else:
                                self.op_exitAtual = 0
                    if event.key == pygame.K_d:
                        if self.op_atual == 4:
                            self.op_atual = 3
                        if self.Exit:
                            if self.op_exitAtual == 1:
                                self.op_exitAtual = 0
                            else:
                                self.op_exitAtual = 1
                    if event.key == pygame.K_RETURN:
                        if self.op_atual == 4:
                            self.Exit = True
                        else:
                            return text[self.op_atual]
                        if self.Exit:
                            if self.op_exitAtual == 1:
                                self.Exit = False
                                self.op_exitAtual = None
                            elif self.op_exitAtual == 0:
                                self.close = True

    # Desenha as opçoes do menu com a cor ciano caso o número da opção seja igual a da variavel de iteração
    def select(self, op_atual, select_list, text):
        self.op_atual = op_atual
        self.select_list = select_list
        self.text = text

        for i in range(len(self.select_list)):
            if i == op_atual:
                self.menu_text(50, self.text[i], COLOR_CIEN, self.select_list[i])
            else:
                self.menu_text(50, self.text[i], COLOR_WHITE, self.select_list[i])

    def select_exit(self, op_exitAtual, exit_listPosition, exit_listText):
        self.op_exitAtual = op_exitAtual
        self.exit_listPosition = exit_listPosition
        self.exit_listText = exit_listText

        for i in range(len(self.exit_listPosition)):
            if i == op_exitAtual:
                self.menu_text(40, self.exit_listText[i], COLOR_CIEN, self.exit_listPosition[i])
            else:
                self.menu_text(40, self.exit_listText[i], COLOR_WHITE, self.exit_listPosition[i])

    def menu_text(self, text_size: int, text: str, color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_position)
        self.window.blit(source=text_surf, dest=text_rect)
