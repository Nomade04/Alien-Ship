#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Animacao import animacao
from code.Const import COLOR_WHITE, WIN_WIDTH, exit_listPosition_level, exit_listText_level, exit_scren_level, \
    exit_rect_level, COLOR_CIEN, WIN_HEIGHT, text, EVENT_ENEMY, ANIM_DELAY
from code.EntityMediator import EntityMediator
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player



class Level:
    def __init__(self, window, name, mode):
        self.atual = 0
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
        self.Shot_animated = pygame.sprite.Group()
        pygame.time.set_timer(EVENT_ENEMY,1000*(random.randint(4,7)))#*(random.randint(2,7))

    def run(self):
        pygame.mixer_music.load('./asset/Sounds/level_1.mp3')
        pygame.mixer_music.play(-1)
        Clock = pygame.time.Clock()


        while True:
            Clock.tick(60)
            EntityMediator.verify_collision(entity_list= self.entity_list)
            EntityMediator.verify_health(entity_list= self.entity_list)

            pressed_k = pygame.key.get_pressed()
            if pressed_k[pygame.K_SPACE]:
                play_shot1 = self.player1.shot()
                if play_shot1 is not None:
                    self.entity_list.append(play_shot1)
            if pressed_k[pygame.K_RCTRL]:
                play_shot2 = self.player2.shot()
                if play_shot2 is not None:
                    self.entity_list.append(play_shot2)

            if not self.Exit:
                for ent in self.entity_list:
                    self.window.blit(source=ent.surf, dest=ent.rect)
                    ent.move()
                    self.Sprites.draw(self.window)
                    self.Sprites.update()
                    self.player1.move(1)
                    if self.mode in [text[1],text[2]]:
                        self.player2.move(2)

                    for ent in self.entity_list:
                        if ent.name == 'Enemy-1':
                            atual =0
                            anim_shot1 = animacao()
                            animated = anim_shot1.animated(1)
                            inicio = pygame.time.get_ticks()
                            atraso = ANIM_DELAY[1]

                            if pygame.time.get_ticks() - inicio >= atraso:
                                atual += 0.5  # (frame/AnimatedTime)
                                if atual >= len(animated):
                                    atual = 0
                                self.window.blit(source=anim_shot1.sprite[int(atual)], dest=ent.rect)



                    if isinstance(ent, Enemy):
                        shot = ent.shot(self.window)
                        if shot is not None:
                            # if ent.name == 'Enemy-1':
                            #     anim_shot1 = animacao(1, ent.rect)
                            #     if anim_shot1.delay():
                            #         self.window.blit(source=anim_shot1.sprite[anim_shot1.atual], dest=ent.rect)
                            #         anim_shot1.update()
                            # animaca = animacao(ent, (self.rect.centerx - 60, self.rect.centery - 5))
                            # Shot_animated.add(animaca)
                            # self.Shot_animated.append()
                            self.entity_list.append(shot)

            if self.Exit:
                self.window.blit(exit_scren_level, exit_rect_level)
                self.menu_text(40, 'Are you sure you want to leave?', COLOR_WHITE, ((WIN_WIDTH / 2), 205))
                self.select_exit(self.op_exitAtual, exit_listPosition_level, exit_listText_level)
                if self.close:
                    pygame.quit()
                    quit()

            self.level_text(20,f"fps: {Clock.get_fps() :.0f}",COLOR_WHITE,(10,WIN_HEIGHT -35))
            self.level_text(25,f'{self.name} Time Out: | {self.TimeOut/1000//60 :.0f}: {self.TimeOut/1000%60 :.0f} m |', COLOR_WHITE,(10,5))
            self.level_text(15, f'Entidades: {len(self.entity_list)-10}', COLOR_WHITE, (10, WIN_HEIGHT -15)  )


            for event in pygame.event.get():
                if event.type == EVENT_ENEMY:
                    number = random.randint(1,3)
                    self.entity_list.append(EntityFactory.get_entity(f'Enemy-1'))#{number}
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