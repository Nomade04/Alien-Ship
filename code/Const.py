#-------------Tamanho da tela------------
import pygame

WIN_WIDTH = 820
WIN_HEIGHT = 480
#-----------------Cores------------------
COLOR_CIEN = [16,239,224]
COLOR_BLACK =[0,0,0]
COLOR_WHITE = [255,255,255]
#----------------Menu--------------------
select_list = []                          #lista com
text = []
exit_listText = ['Yes', 'No']
exit_listPosition = [(250,260),(570,260)]
text.append("New Game")
text.append("New game - 2P Coop")
text.append("New game - 2P PvP")
text.append("Score")
text.append("EXIT")
exit_scren = pygame.image.load('./asset/MenuFrame/EXIT_scren.png')
exit_rect = exit_scren.get_rect(left=(150), top=60)
exit_scren = pygame.transform.scale(exit_scren, (510, 400))
select_list.append(((WIN_WIDTH / 2), 300))
select_list.append(((WIN_WIDTH / 2), 340))
select_list.append(((WIN_WIDTH / 2), 380))
select_list.append(((WIN_WIDTH / 2), 420))
select_list.append(((WIN_WIDTH - 760), 460))
#----------------lEVEL----------------------
ENTITY_SPEED = {
    'Level 1_0': 0,
    'Level 1_1': 1,
    'Level 1_2': 2,
    'Level 1_3': 3,
    'Level 1_4': 4,
    'Enemy-1': 1,
    'Enemy-2': 2,
    'Enemy-3': 3,
    'Enemy-1Shot': 6,
    'Enemy-2Shot': 7,
    'Enemy-3Shot': 9,
    'Player-Shot2': 10

}
exit_rect_level = exit_scren.get_rect(left=(150), top=35)
exit_scren_level = pygame.transform.scale(exit_scren, (510, 480))
exit_listText_level = ['Yes', 'No', 'Return to menu']
exit_listPosition_level = [(250,260),(570,260),(413,300)]
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_RESPAW = pygame.USEREVENT + 2
PLAYER_CHEK = pygame.USEREVENT + 3

ENTITY_HEALTH = {
    'Level 1_0': 999,
    'Level 1_1': 999,
    'Level 1_2': 999,
    'Level 1_3': 999,
    'Level 1_4': 999,
    'Enemy-1': 6,
    'Enemy-2': 8,
    'Enemy-3': 3,
    'Player-Shot2': 1,
    'Enemy-1Shot': 1,
    'Enemy-2Shot': 1,
    'Enemy-3Shot': 1,

}

SHOT_DELAY = {
    'Enemy-1': 80,
    'Enemy-2': 70,
    'Enemy-3': 60,

}
