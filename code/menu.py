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
        self.surf = pygame.image.load('./asset/Titulo_Game2.png')
        self.rect = self.surf.get_rect(left=(WIN_WIDTH/4), top=75)
        self.surf =pygame.transform.scale(self.surf,(655/1.5,211/1.5))
        self.op_atual = 0
    def run(self):
        pygame.mixer_music.load('./asset/cosmos.mp3')
        pygame.mixer.music.play(-1)

        while True:
            # checando todos os eventos
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()  # Fecha a janela do jogo
                    quit()  # Fecha o pygame
                if event.type == pygame.KEYDOWN:
                    print(event.key)
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


            Animacao.draw(self.window)
            Animacao.update()
            self.window.blit(source=self.surf, dest=self.rect)
            self.select(self.op_atual,select_list,text)

            pygame.display.flip()

        pass

    def select(self,op_atual, select_list, text):
        self.op_atual = op_atual
        self.select_list = select_list
        self.text = text


        for i in range(len(self.select_list)):

            if i == op_atual:
                self. menu_text(50,self.text[i],COLOR_CIEN,self.select_list[i])
            else:
                self.menu_text(50, self.text[i], COLOR_WHITE, self.select_list[i])


    def menu_text(self, text_size: int, text: str, color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size = text_size)
        text_surf: Surface = text_font.render(text,True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_position)
        self.window.blit(source=text_surf, dest=text_rect)

