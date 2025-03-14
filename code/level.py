#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import COLOR_WHITE, WIN_WIDTH, exit_listPosition_level, exit_listText_level, exit_scren_level, \
    exit_rect_level, COLOR_CIEN, WIN_HEIGHT, text
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player



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
        self.Sprites = pygame.sprite.Group()
        if self.mode in [text[1],text[2]]:
            self.player2 = Player(2)
            self.Sprites.add(self.player2)
        self.player1 = Player(1)
        self.Sprites.add(self.player1)
        self.TimeOut = 300000

    def run(self):
        pygame.mixer_music.load('./asset/Sounds/level_1.mp3')
        pygame.mixer_music.play(-1)
        Clock = pygame.time.Clock()


        while True:
            Clock.tick(60)

            if not self.Exit:
                for ent in self.entity_list:
                    self.window.blit(source=ent.surf, dest=ent.rect)
                    ent.move()
                    self.Sprites.draw(self.window)
                    self.Sprites.update()
                    self.player1.move(1)
                    if self.mode in [text[1],text[2]]:
                        self.player2.move(2)


            if self.Exit:
                self.window.blit(exit_scren_level, exit_rect_level)
                self.menu_text(40, 'Are you sure you want to leave?', COLOR_WHITE, ((WIN_WIDTH / 2), 205))
                self.select_exit(self.op_exitAtual, exit_listPosition_level, exit_listText_level)
                if self.close:
                    pygame.quit()
                    quit()

            self.level_text(20,f"fps: {Clock.get_fps() :.0f}",COLOR_WHITE,(10,WIN_HEIGHT -35))
            self.level_text(25,f'{self.name} Time Out: | {self.TimeOut/1000//60 :.0f}: {self.TimeOut/1000%60 :.0f} m |', COLOR_WHITE,(10,5))
            self.level_text(15, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT -15)  )


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Exit = True
                if event.type == pygame.KEYDOWN:
                    if self.Exit:
                        if event.key == pygame.K_a:
                            self.op_exitAtual = 0
                        if event.key == pygame.K_d:
                            self.op_exitAtual = 1
                        if event.key == pygame.K_s:
                            self.op_exitAtual = 2
                    if event.key == pygame.K_RETURN:
                        if self.op_exitAtual == 1:
                            self.Exit = False
                            self.op_exitAtual = None
                        elif self.op_exitAtual == 0:
                            self.close = True
                        elif self.op_exitAtual == 2:
                            self.op_exitAtual = None
                            return
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

    def level_text(self, text_size: int, text: str, color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left =text_pos[0],top =text_pos[1] )
        self.window.blit(source=text_surf, dest=text_rect)