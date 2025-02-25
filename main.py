import pygame as pg

print("Setup start")
pg.init()

# Criando a janela do jogo com o parametro Tamanho
window = pg.display.set_mode(size=(600, 480))
print("Setup end")

print("loop start")
while True:
    # checando todos os eventos
    for event in pg.event.get():
        if event == pg.QUIT:
            pg.quit()  # Fecha a janela do jogo
            quit()  # Fecha o pygame
