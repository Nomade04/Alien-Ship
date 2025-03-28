#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import menu
from code.Animacao import animacao
from code.Const import COLOR_WHITE, WIN_WIDTH, exit_listPosition_level, exit_listText_level, exit_scren_level, \
    exit_rect_level, COLOR_CIEN, WIN_HEIGHT, text, EVENT_ENEMY, ANIM_DELAY, EVENT_RESPAW, PLAYER_CHEK
from code.EnemyShot import EnemyShot
from code.EntityMediator import EntityMediator
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player



class Level:
    def __init__(self, window, name, mode):
        self.player_life = []
        self.last_event = pygame.time.get_ticks()
        self.respawn_time = 8000
        self.event_respawn = False
        self.rum = False
        self.atual = 0
        self.close = None
        self.op_exitAtual = None
        self.Exit = False
        self.window = window
        self.name = name
        self.mode = mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level'))
        self.players = []
        self.Sprites = pygame.sprite.Group()
        self.SpriteShot = pygame.sprite.Group()
        if self.mode in [text[1],text[2]]:
            self.player2 = Player(2)
            self.Sprites.add(self.player2)
            self.players.append(self.player2)

        self.player1 = Player(1)
        self.Sprites.add(self.player1)
        self.players.append(self.player1)
        self.TimeOut = 300000
        self.Shot_animated = pygame.sprite.Group()
        self.animation1 = animacao(1)
        pygame.time.set_timer(PLAYER_CHEK,100)

        pygame.time.set_timer(EVENT_ENEMY,1000*(random.randint(4,7)))#*(random.randint(2,7))

    def run(self):
        pygame.mixer_music.load('./asset/Sounds/level_1.mp3')
        pygame.mixer_music.play(-1)
        Clock = pygame.time.Clock()


        while True:
            Clock.tick(60)
            time_now = pygame.time.get_ticks()

            EntityMediator.verify_collision(players=self.players, entity_list= self.entity_list)
            EntityMediator.verify_health(entity_list= self.entity_list)
            # print(self.respawn_time)
            # print(len(self.Sprites))
            pressed_k = pygame.key.get_pressed()
            for i in range(len(self.players)):
                if self.players[i].instance:
                    if pressed_k[pygame.K_SPACE]:
                        play_shot1 = self.player1.shot()
                        if play_shot1 is not None:
                            self.entity_list.append(play_shot1)
                if self.players[i].number == 2:
                    if self.players[i].instance:
                        if pressed_k[pygame.K_RCTRL]:
                            play_shot2 = self.player2.shot()
                            if play_shot2 is not None:
                                self.entity_list.append(play_shot2)

            if not self.Exit:

                for i in range(len(self.players)):
                    if self.players[i].health <= 0:
                        self.Sprites.remove(self.players[i])
                        self.players[i].instance = False
                #         self.event_respawn = True
                #
                #
                # if len(self.Sprites) == self.mode:
                #     self.event_respawn = False
                #
                # if self.event_respawn:
                #     pygame.time.set_timer(EVENT_RESPAW, 10000)


                # print(self.player1.health)

                for ent in self.entity_list:
                    self.window.blit(source=ent.surf, dest=ent.rect)

                    ent.move()
                    self.Sprites.draw(self.window)
                    self.Sprites.update()
                    for i in range(len(self.players)):
                        if self.players[i].instance:
                            self.window.blit(source=self.players[i].HudPicture, dest=self.players[i].HudRect)
                            self.players[i].HubHeart(self.window)

                        if not self.players[i].instance:
                            respaningIn = self.respawn_time - (time_now - self.last_event)
                            self.level_text(20, f"Respawning in... {respaningIn//1000}", COLOR_WHITE, (self.players[i].HudRect[0],self.players[i].HudRect[1] + 25))



                    self.player1.move(1)
                    if self.mode in [text[1],text[2]]:
                        self.player2.move(2)

                    if isinstance(ent, Enemy):
                        shot = ent.shot()
                        if shot is not None:
                            self.entity_list.append(shot)
                    # for entshot in self.entity_list:
                    #     if isinstance(entshot, EnemyShot):
                    #         animation1 = animacao(1)
                    #         animation1.rect.topleft = entshot.initial
                    #
                    #         if not animation1.finished:  # Só desenha se a animação não terminou
                    #             self.window.blit(animation1.image, animation1.rect)
                    #             animation1.update()
                    #         else:
                    #             self.entity_list.remove(entshot)

                                # animacao.draw(animation1)

                        # if ent.name =='Enemy-1':
                        #
                        #     self.SpriteShot.draw(self.window)
                        #     self.SpriteShot.update()
                            # animation1.move(1)
                            # print(self.SpriteShot)
                            # for spr in self.SpriteShot:
                            #     print(spr.atual)
                            #     if spr.atual >= 3:
                            #         self.SpriteShot.remove(spr)


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
                    self.entity_list.append(EntityFactory.get_entity(f'Enemy-{number}'))#{number}

                if event.type == PLAYER_CHEK:
                    for i in range(len(self.players)):
                        if not self.players[i].instance:
                            self.event_respawn = True

                    if self.mode == menu.text[0]:
                        planum = 1
                    else:
                        planum = 2
                    if len(self.Sprites) == planum:
                        self.event_respawn = False

                    for i in range(len(self.players)):
                        if not self.players[i].instancing:
                            if self.event_respawn:
                                pygame.time.set_timer(EVENT_RESPAW, self.respawn_time)
                                self.last_event = pygame.time.get_ticks()
                                self.players[i].instancing = True

                if event.type == EVENT_RESPAW:


                    for i in range(len(self.players)):
                        if not self.players[i].instance:
                            self.players[i].rect.topleft = self.players[i].respaw_point
                            self.players[i].health = self.players[i].respaw_health
                            self.Sprites.add(self.players[i])
                            pygame.time.set_timer(EVENT_RESPAW, 0)
                            self.players[i].instancing = False
                            self.players[i].instance = True

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