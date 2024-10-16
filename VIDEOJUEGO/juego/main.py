import asyncio
import pygame
import sys
import json
from clases.sqlfuntion import SQLFuntion
from clases.block import Block
from clases.usuario import NameInputScreen
from clases.game import Game
from clases.menu import Menu
from clases.dicc import diccionario


# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana y del tablero
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bloxorz 2D")

pygame.mixer.init()
music_num = 0

# Crear objeto SQLFuntion para manejar las operaciones con la base de datos
sql_base = SQLFuntion()


# Obtener el último movimiento de la base de datos
historial_id, time_insert, level, orientacion, x, y, board = sql_base.obtener_informacion_movimientos()
block = Block(x, y, 40, orientacion)
game = Game(screen, block, level, sql_base, historial_id, json.loads(board))
menu = Menu(screen)
user = NameInputScreen(screen)


# Ciclo principal del juego
async def main():
    global game
    global menu
    global user
    global music_num
    while True:
        if music_num == 0:
            pygame.mixer.music.load("Sounds/espera.ogg")
            pygame.mixer.music.play(-1)
            music_num = 1

        # Manejar la pantalla de ingreso del nombre del usuario
        if not user.finished:
            user.update_image()
            user.draw()

        # Manejar el menú
        if not menu.finished and user.finished:
            menu.update()
            menu.draw()
            game.block.play = menu.play

        # Manejar el juego y el menú
        if not game.play and menu.finished:
            game.update()
            game.draw()

            if music_num == 1:
                pygame.mixer.music.load("Sounds/Bloxorz.ogg")
                pygame.mixer.music.play(-1)
                music_num = 2

            if game.retornar() or game.level == len(diccionario):
                music_num = 0
                menu.set_menu()
                if game.level == len(diccionario):
                    game.reset_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not user.finished:
                user.update(event)

        pygame.time.Clock().tick(60)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
