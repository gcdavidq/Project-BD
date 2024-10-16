import pygame
from clases.dicc import diccionario
from clases.button import Button
from clases.direc import DirectionButtons
import numpy as np
from datetime import datetime
import json
import time

"""
Módulo game
"""

class Game:
    """
        Representa el estado y lógica del juego.

        Attributes:
        -----------
        screen : pygame.Surface
            La superficie de la pantalla donde se renderiza el juego.
        block : Block
            El bloque que el jugador mueve en el juego.
        level : int
            El nivel actual del juego.
        sql_bas : SQLDatabase
            Objeto para interactuar con la base de datos del juego.
        historial_id : int
            Identificador del historial del juego.
        board : list
            Lista que representa el estado del tablero.
        goal_pos : tuple
            Coordenadas del objetivo que el jugador debe alcanzar.
        TILE_SIZE : int
            Tamaño de cada celda del tablero.
        play : bool
            Indica si el juego está activo.
        wingame : bool
            Indica si el jugador ha ganado.
        lossgame : bool
            Indica si el jugador ha perdido.
        button_return : Button
            Botón para regresar al menú principal.
        background_image : pygame.Surface
            Imagen de fondo del juego.
        direction : DirectionButtons
            Botones que controlan la dirección del bloque.
        block_image, block_X, block_O, block_D : pygame.Surface
            Imágenes que representan distintos tipos de bloques.
        w : int
            Posición horizontal inicial para centrar el tablero.
        h : int
            Posición vertical inicial del tablero.
        up : int
            Variable que ajusta el nivel cuando se gana una partida.
        sound_block, death, acti, win : pygame.mixer.Sound
            Efectos de sonido del juego.
        anterior : list
            Posiciones anteriores del bloque.
        sql_base : SQLDatabase
            Objeto para realizar operaciones en la base de datos.
        ante_hisorial_id : int
            Identificador del historial anterior.

        Methods:
        --------
        __init__(self, screen: pygame.Surface, block: Block, level: int, sql_bas: SQLDatabase, historial_id: int, board: list) -> None:
            Inicializa el juego con el nivel, pantalla, bloque y demás atributos iniciales.

        reset_game(self) -> None:
            Reinicia el juego y coloca el tablero en su estado inicial según el nivel.

        is_valid_position(self) -> bool:
            Verifica si la posición actual del bloque es válida en el tablero.

        draw_board(self) -> None:
            Dibuja el tablero en la pantalla con las texturas y bordes correspondientes.

        retornar(self) -> bool:
            Verifica si se ha presionado el botón de regreso.

        update(self) -> None:
            Actualiza el estado del juego y las interacciones con la base de datos.

        draw(self) -> None:
            Dibuja todos los elementos del juego, incluyendo el tablero, el bloque y los botones.
        """
    def __init__(self, screen, block, level, sql_bas, historial_id, board):
        """
            Inicializa la clase Game con los parámetros dados.

            Parámetros:
            -----------
            screen : pygame.Surface
                La superficie de Pygame donde se dibuja el juego.
            block : Block
                El bloque controlado por el jugador.
            level : int
                El nivel del juego.
            sql_bas : SQLConnection
                Objeto de conexión a la base de datos para guardar el progreso.
            historial_id : int
                ID de historial para registrar el progreso del juego.
            board : list
                La representación del tablero en formato de lista.
        """
        self.level = level
        self.screen = screen
        self.goal_pos = (diccionario[self.level]['objetivo'][0], diccionario[self.level]['objetivo'][1])
        self.block = block
        self.TILE_SIZE = block.TILE_SIZE
        self.list_to = board
        self.board = np.array(self.list_to)
        self.play = False
        self.wingame = False
        self.lossgame = False
        self.button_return = Button(screen.get_width() - 100, screen.get_height() - 50,"BACK", 20, 70, 40)  # objeto de la clse Button
        self.background_image = pygame.transform.scale(pygame.image.load("Graphics/game.png"), (screen.get_width(), screen.get_height()))
        self.direction = DirectionButtons(screen)
        self.block_image = pygame.transform.scale(pygame.image.load("Graphics/textura.png"), (self.TILE_SIZE, self.TILE_SIZE))  # Escalar la imagen al tamaño del cuadro
        self.block_X = pygame.transform.scale(pygame.image.load("Graphics/textura_X.png"), (self.TILE_SIZE, self.TILE_SIZE))  # Escalar la imagen al tamaño del cuadro
        self.block_O = pygame.transform.scale(pygame.image.load("Graphics/textura_o.png"), (self.TILE_SIZE, self.TILE_SIZE))  # Escalar la imagen al tamaño del cuadro
        self.block_D = pygame.transform.scale(pygame.image.load("Graphics/textura_d.png"), (self.TILE_SIZE, self.TILE_SIZE))  # Escalar la imagen al tamaño del cuadro
        self.w = (self.screen.get_width() - len(self.board[0]) * self.TILE_SIZE) // 2
        self.h = 50
        self.up = 0
        self.sound_block = pygame.mixer.Sound('Sounds/sound_block.ogg')
        self.death = pygame.mixer.Sound('Sounds/Death.ogg')
        self.acti = pygame.mixer.Sound('Sounds/acti.ogg')
        self.win = pygame.mixer.Sound('Sounds/win.ogg')
        self.anterior = None
        self.sql_base = sql_bas
        self.historial_id = historial_id
        self.ante_hisorial_id = historial_id

    def reset_game(self):
        """
            Reinicia el bloque y el tablero para el nivel actual.
        """
        self.block.reset_block(self.level + self.up)
        if not self.block.active or self.wingame:
            self.board = np.array(diccionario[self.level+self.up]['tablero'])
            self.board, self.list_to = np.array(self.list_to), self.board.tolist()


    def is_valid_position(self):
        """
            Verifica si la posición del bloque es válida en el tablero.

            Devuelve:
            ---------
            bool:
                True si la posición es válida, False en caso contrario.
        """
        positions = self.block.get_positions()
        if self.anterior != positions:
            for pos in positions:
                x, y = pos
                # Si alguna parte del bloque está fuera del tablero
                if x < 0 or y < 0 or x >= self.board.shape[1] or y >= self.board.shape[0]:
                    return False

                # Si alguna parte del bloque está en una casilla negra (excepto el destino)
                if self.board[y][x] <= 0 and pos != self.goal_pos:
                    return False

                if self.board[y][x] == 4 and self.block.orientation == 'punto':
                    return False

                else:
                    if self.anterior != positions:
                        if int(self.board[y][x]) == 2:
                            self.board[abs(self.board) == 1+(self.board[y][x]/10)] = -self.board[abs(self.board) == 1+(self.board[y][x]/10)]
                            self.acti.play()

                        elif int(self.board[y][x]) == 3 and self.block.orientation_prue == 'punto':
                            self.board[abs(self.board) == 1 + (self.board[y][x] / 10)] = -self.board[abs(self.board) == 1 + (self.board[y][x] / 10)]
                            self.acti.play()

                        elif int(self.board[y][x]) == 5:
                            self.board[abs(self.board) == round(self.board[y][x] - 4, 2)] = -abs(self.board[abs(self.board) == round(self.board[y][x] - 4, 2)])
                            self.acti.play()
            self.board, self.list_to = np.array(self.list_to), self.board.tolist()
            self.anterior = positions
            self.sound_block.play()
        return True

    def draw_board(self):
        """
            Dibuja el tablero del juego en la pantalla.
        """
        self.w = (self.screen.get_width() - len(self.board[0]) * self.TILE_SIZE) // 2
        self.h = 50
        for y, row in enumerate(self.board):
            for x, tile in enumerate(row):
                if int(tile) == 1:  # Si es una casilla válida (suelo)
                    self.screen.blit(self.block_image, (self.w + (x * self.TILE_SIZE), self.h + (y * self.TILE_SIZE)))  # Dibuja la imagen
                elif int(tile) == 2 or int(tile) == 5:# Suelo con un circulo
                    self.screen.blit(self.block_O, (self.w + (x * self.TILE_SIZE), self.h + (y * self.TILE_SIZE)))  # Dibuja la imagen
                elif int(tile) == 3:# Suelo con una X
                    self.screen.blit(self.block_X, (self.w + (x * self.TILE_SIZE), self.h + (y * self.TILE_SIZE)))  # Dibuja la imagen
                elif tile == 4:#Suelo desprendible(crema)
                    self.screen.blit(self.block_D, (self.w + (x * self.TILE_SIZE), self.h + (y * self.TILE_SIZE)))  # Dibuja la imagen
                if tile > 0:
                    pygame.draw.rect(self.screen, (192, 192, 192), (self.w + (x * self.TILE_SIZE), self.h + (y * self.TILE_SIZE), self.TILE_SIZE, self.TILE_SIZE),1)  # Borde
        pygame.draw.rect(self.screen, (255, 0, 0), (self.w + (self.goal_pos[0] * self.TILE_SIZE), self.h + (self.goal_pos[1] * self.TILE_SIZE), self.TILE_SIZE, self.TILE_SIZE))

    def retornar(self):
        """
            Verifica si el botón de retorno ha sido pulsado.

            Devuelve:
            ---------
            bool:
                True si el botón de retorno ha sido pulsado, False en caso contrario.
        """
        if self.button_return.clicked: # si el boton play es tocado, cambiar button_return a True
            return True

    def update(self):
        """
            Actualiza el estado del juego.

            Esta función gestiona la dirección del bloque según las entradas, verifica la validez de
            la posición del bloque en el tablero, actualiza el historial en la base de datos, y maneja
            la lógica de las votaciones y las transiciones entre estados (victoria o pérdida).

            Si el bloque alcanza la posición objetivo o si el jugador pierde, el juego se reinicia.
            También recupera el estado del juego cada 5 segundos para actualizar la posición del bloque
            desde la base de datos.
        """
        self.direction.position_update()
        if self.historial_id == self.ante_hisorial_id:
            self.block.update(self.direction.direction)
        self.direction.direction = ""
        self.button_return.update()
        if self.block.play:
            self.direction.update()
        if self.block.voto != '5':
            self.block.active = True

        # Verificar si la posición es válida después de cada movimiento
        if not self.is_valid_position() and not self.wingame:
            self.lossgame = True
            self.reset_game()
        elif (self.block.x_pru, self.block.y_pru) == self.goal_pos and self.block.orientation_prue == 'punto':
            self.up = 1
            self.wingame = True
            self.reset_game()

        if self.block.voto != '5':
            # Ejecutar la actualización en segundo plano
            self.sql_base.actualizar_registro(self.block.voto, self.historial_id, self.level+self.up, self.block.orientation_prue,
                                         self.block.x_pru, self.block.y_pru, json.dumps(self.list_to))
            print(self.block.orientation_prue, self.block.x_pru, self.block.y_pru)
            #print("luego de igualar", self.block.orientation, self.block.x, self.block.y)
            self.historial_id = None
            self.block.voto = '5'

        # Cada 5 segundos obtener la información de movimientos en segundo plano
        if (datetime.now().second + 1) % 10 == 0:
            print('votacion cerrada')
            print("llamando nuevos valores")
            self.historial_id, time_insert, self.level, self.block.orientation, self.block.x, self.block.y, self.list_to = self.sql_base.obtener_informacion_movimientos()
            self.list_to = json.loads(self.list_to)
            print(time_insert)
            if self.ante_hisorial_id != self.historial_id:
                print("nuevo estado: ", self.block.orientation, self.block.x, self.block.y)
                self.block.orientacion_prue = self.block.orientation
                self.block.x_pru, self.block.y_pru = self.block.x, self.block.y
                if self.block.active:
                    self.anterior = None
                self.block.active = False
                if self.lossgame:
                    self.death.play()
                    self.reset_game()
                    self.lossgame = False
                self.up = 0
                self.goal_pos = (diccionario[self.level]['objetivo'][0], diccionario[self.level]['objetivo'][1])
                self.ante_hisorial_id = self.historial_id
            else:
                print('No hay movimiento')
            time.sleep(1)
            print('Vuelve a votar')


    def draw(self):
        """
            Dibuja todos los elementos en la pantalla.

            Esta función dibuja el tablero, el bloque, los botones, y gestiona el temporizador de votación,
            que se muestra en la pantalla durante el juego. También reproduce sonidos si el jugador gana.
        """
        # Dibujar todo
        self.screen.blit(self.background_image, (0, 0))
        self.draw_board()
        self.button_return.draw(self.screen)

        if self.block.play:
            self.direction.draw()

        self.block.draw(self.screen, self.w, self.h)

        # Obtener el segundo actual
        current_time = datetime.now().second

        # Definir el texto basado en la condición
        if (current_time + 1) % 10 != 9:
            tiempo_votacion = f"Tiempo de la votación: {(10-current_time)%10 - 2}"
        else:
            tiempo_votacion = "Votación terminada, espere..."

        # Renderizar el texto
        font = pygame.font.SysFont('Arial', 30)  # Fuente para el texto
        texto_superficie = font.render(tiempo_votacion, True, (255, 255, 255))  # Texto en blanco
        texto_rect = texto_superficie.get_rect(
            center=(self.screen.get_width() // 2, 420))  # Centrar en la parte superior

        # Dibujar el texto en la pantalla
        self.screen.blit(texto_superficie, texto_rect)

        # Comprobar si ha llegado al objetivo
        if self.wingame and self.up == 0:
            self.win.play()
            self.reset_game()
            self.wingame = False

        pygame.display.flip()
    pass