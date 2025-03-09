#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from pygame.locals import *
from code.Const import *
from code.MenuAnimated import MenuAnimate

Animacao = pygame.sprite.Group()
AnimacaoMenu = MenuAnimate()
Animacao.add(AnimacaoMenu)
select_list = []
text = []
exit_listText = ['Yes', 'No']
exit_listPosition = [(250,260),(570,260)]
text.append("New Game")
text.append("New game - 2P Coop ")
text.append("New game - 2P PvP ")
text.append("Score")
text.append("EXIT")
select_list.append(((WIN_WIDTH / 2), 300))
select_list.append(((WIN_WIDTH / 2), 340))
select_list.append(((WIN_WIDTH / 2), 380))
select_list.append(((WIN_WIDTH / 2), 420))
select_list.append(((WIN_WIDTH - 760), 460))

class Menu:
    def __init__(self, window):
        self.window = window
        self.title = pygame.image.load('./asset/Titulo_Game2.png')
        self.rect = self.title.get_rect(left=(WIN_WIDTH/4), top=75)
        self.title = pygame.transform.scale(self.title,(655/1.5,211/1.5))
        self.op_atual = 0
        self.op_exitAtual = None
        self.Exit = None
        self.close = None
        self.exit_scren = pygame.image.load('./asset/EXIT_scren.png')
        self.exit_rect = self.exit_scren.get_rect(left=(150),top =60)
        self.exit_scren = pygame.transform.scale(self.exit_scren, (510, 400 ))
    def run(self):
        pygame.mixer_music.load('./asset/cosmos.mp3')
        pygame.mixer.music.play(-1)

        while True:
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
                        if self.Exit:
                            if self.op_exitAtual == 1:
                                self.Exit = False
                                self.op_exitAtual = None
                            elif self.op_exitAtual == 0:
                                self.close = True





            Animacao.draw(self.window)
            Animacao.update()
            self.window.blit(source=self.title, dest=self.rect)
            if self.Exit:
                self.window.blit(self.exit_scren, self.exit_rect)
                self.menu_text(40,'Are you sure you want to leave?', COLOR_WHITE,((WIN_WIDTH / 2), 205) )
                self.select_exit(self.op_exitAtual,exit_listPosition, exit_listText)
                if self.close:
                    pygame.quit()  # Fecha a janela do jogo
                    quit()
            else:
                self.select(self.op_atual, select_list, text)

            pygame.display.flip()

        pass

    def select(self,op_atual, select_list, text):
        self.op_atual = op_atual
        self.select_list = select_list
        self.text = text

        for i in range(len(self.select_list)):
            print(op_atual)
            if i == op_atual:
                self. menu_text(50,self.text[i],COLOR_CIEN,self.select_list[i])
            else:
                self.menu_text(50, self.text[i], COLOR_WHITE, self.select_list[i])
    def select_exit(self,op_exitAtual, exit_listPosition, exit_listText):
        self.op_exitAtual = op_exitAtual
        self.exit_listPosition = exit_listPosition
        self.exit_listText = exit_listText

        for i in range(len(self.exit_listPosition)):
            print(op_exitAtual)
            if i == op_exitAtual:
                self. menu_text(40,self.exit_listText[i],COLOR_CIEN,self.exit_listPosition[i])
            else:
                self.menu_text(40, self.exit_listText[i], COLOR_WHITE, self.exit_listPosition[i])


    def menu_text(self, text_size: int, text: str, color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size = text_size)
        text_surf: Surface = text_font.render(text,True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_position)
        self.window.blit(source=text_surf, dest=text_rect)

