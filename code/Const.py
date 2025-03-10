#-------------Tamanho da tela------------
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
text.append("New game - 2P Coop ")
text.append("New game - 2P PvP ")
text.append("Score")
text.append("EXIT")
select_list.append(((WIN_WIDTH / 2), 300))
select_list.append(((WIN_WIDTH / 2), 340))
select_list.append(((WIN_WIDTH / 2), 380))
select_list.append(((WIN_WIDTH / 2), 420))
select_list.append(((WIN_WIDTH - 760), 460))
#----------------lEVEL----------------------
ENTITY_SPEED = {
    'level_1': 0,
    'level_2': 2,
    'level_3': 4,
    'level_4': 6,
    'level_5': 8,
}