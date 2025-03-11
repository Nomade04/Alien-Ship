#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import event
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import COLOR_WHITE, WIN_WIDTH, exit_listPosition, exit_listText, exit_scren, exit_rect, COLOR_CIEN
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.menu import Menu


class Level:
    def __init__(self, window, name, mode):
        self.close = None
        self.op_exitAtual = None
        self.Exit = False
        self.window = window
        self.name = name
        self.mode = mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level'))

    def run(self):
        while True:
            if not self.Exit:
                for ent in self.entity_list:
                    self.window.blit(source=ent.surf, dest=ent.rect)
                    ent.move()
            if self.Exit:
                self.window.blit(exit_scren, exit_rect)
                self.menu_text(40, 'Are you sure you want to leave?', COLOR_WHITE,  ((WIN_WIDTH / 2), 205))
                self.select_exit(self.op_exitAtual, exit_listPosition, exit_listText)
                if self.close:
                    pygame.quit()
                    quit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Exit = True
                if event.type == pygame.KEYDOWN:
                    if self.Exit:
                        if event.key == pygame.K_a:
                            self.op_exitAtual = 0
                        if event.key == pygame.K_d:
                            self.op_exitAtual = 1

                    if event.key == pygame.K_RETURN:
                        if self.op_exitAtual == 1:
                            self.Exit = False
                            self.op_exitAtual = None
                        elif self.op_exitAtual == 0:
                            self.close = True
            pygame.display.flip()
    def menu_text(self, text_size: int, text: str, color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_position)
        self.window.blit(source=text_surf, dest=text_rect)

    def select_exit(self, op_exitAtual, exit_listPosition, exit_listText):
        self.op_exitAtual = op_exitAtual
        self.exit_listPosition = exit_listPosition
        self.exit_listText = exit_listText

        for i in range(len(self.exit_listPosition)):
            if i == op_exitAtual:
                self.menu_text(40, self.exit_listText[i], COLOR_CIEN, self.exit_listPosition[i])
            else:
                self.menu_text(40, self.exit_listText[i], COLOR_WHITE, self.exit_listPosition[i])
