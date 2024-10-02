import pygame, sys, os, numpy as np

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana y del tablero
WIDTH, HEIGHT = 800, 600

# Colores
RED = (255, 0, 0)
LIGHT_GRAY = (192, 192, 192)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.mixer.init()
nivel = 1
music_num = 0

def resource_path(relative_path):
    """ Obtiene el path absoluto para archivos cuando se usa PyInstaller. """
    try:
        # PyInstaller crea una carpeta temporal y almacena el path dentro de _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)




diccionario = {1:{'inicial': (1, 1),
                  'tablero': [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                              [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                              [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]],
                  'objetivo': (7, 4)},
                2:{'inicial': (1, 4),
                  'tablero': [[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                              [1, 1, 1, 1, 0, 0, 1, 1, 3.1, 1, 0, 0, 1, 0, 1],
                              [1, 1, 2.1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                              [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                              [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, -1.31, -1.31, 1, 1, 1],
                              [1, 1, 1, 1, -1.21, -1.21, 1, 1, 1, 1, 0, 0, 0, 0, 0]],
                  'objetivo': (13, 1)},
                3:{'inicial': (1, 3),
                  'tablero': [[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                              [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                              [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                              [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]],
                  'objetivo': (13, 3)},
                4:{'inicial': (1, 5),
                  'tablero': [[0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0],
                              [0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0],
                              [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                              [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                              [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                              [1, 1, 1, 0, 0, 1, 1, 1, 1, 4, 4, 4, 4, 4],
                              [1, 1, 1, 0, 0, 1, 1, 1, 1, 4, 4, 4, 4, 4],
                              [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 4, 4, 1, 4],
                              [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 4, 4, 4, 4]],
                  'objetivo': (6, 7)},
                5:{'inicial': (0, 3),
                  'tablero': [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                              [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                              [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]],
                  'objetivo': (13, 4)},
                6:{'inicial':(13,1),
                  'tablero':[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                             [0, 1, 1, 1, 1, -1.21, -1.21, 1, 2.1, 1, 1, 1, 1, 1, 1],
                             [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                             [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 1, 1, 5.22, 1, 1, 1, 1, 1, 1, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2.2],
                             [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                             [1, 0, 1, 1, 1, 1.22, 1.22, 1, 1, 1, 1, 1, 1, 0, 0],
                             [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
                  'objetivo':(1,8)},

                 7:{'inicial':(1,3),
                  'tablero':[[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                             [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                             [1, 1, 1, 0, 0, 0, 0, 1, 1, 3.1, 0, 0, 1, 1, 1],
                             [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
                             [0, 1, 1, -3.1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]],
                  'objetivo':(13,3)},

                 8:{'inicial':(1,3),
                  'tablero':[[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                             [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
                             [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                             [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
                             [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
                             [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                             [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]],
                  'objetivo':(14,3)}
               }








class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.fondo_bienvenida = pygame.transform.scale(pygame.image.load(resource_path('Graphics/fondo.png')).convert(), (screen.get_width(), screen.get_height()))
        self.finished= False
        self.exit = False
        self.jugar = False
        self.button_play = Button((screen.get_width() // 2)-100, screen.get_height() // 2, "JUGAR")  # objeto de la clse Button
        self.button_ver = Button((screen.get_width() // 2) - 100, screen.get_height() // 2 + 70,"VER")  # objeto de la clse Button
        self.button_exit = Button((screen.get_width() // 2) - 100, (screen.get_height() // 2) + 140, "EXIT")  # objeto de la clse Button

    def set_menu(self):
        self.finished = False

    def update(self):
        if self.button_play.clicked: # si el boton play es tocado, cambiar menu_finished a True
            self.finished = True
            self.jugar = True
        if self.button_ver.clicked: # si el boton play es tocado, cambiar menu_finished a True
            self.finished = True
            self.jugar = False
        if self.button_exit.clicked: # si el boton play es tocado, cambiar menu_finished a True
            self.exit = True
        self.button_play.update()
        self.button_ver.update()
        self.button_exit.update()

    def draw(self):
        self.screen.blit(self.fondo_bienvenida, (0, 0))
        self.button_play.draw(self.screen)
        self.button_ver.draw(self.screen)
        self.button_exit.draw(self.screen)
        pygame.display.flip()



# obtenido de: https://docs.hektorprofe.net/pygame/escenas-gui/multiples-botones/
class Button:
    def __init__(self, x=0, y=0, text="", size=24, width=200, height=50, image=None, elev=6):
        self.font = pygame.font.Font(resource_path('fonts/04B03.ttf'), size)
        self.text = self.font.render(text, True, "#ffffff")
        self.text_rect = self.text.get_rect()

        # Si se pasa una imagen, se ajusta al tamaño
        self.image = image
        if image:
            self.image = pygame.transform.scale(image, (width, height))

        self.bottom_rect = pygame.Rect((x+elev, y+elev), (width, height))
        self.top_rect = pygame.Rect((x, y), (width, height))
        self.text_rect.center = self.top_rect.center

        self.hover = False
        self.pressed = False
        self.clicked = False
        self.sound_click = pygame.mixer.Sound(resource_path('Sounds/click.mp3'))

    def update(self):
        self.clicked = False
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.hover = True
            if pygame.mouse.get_pressed()[0]:  # Si se presiona el botón izquierdo del mouse
                self.pressed = True
            else:
                if self.pressed:
                    self.pressed = False
                    self.clicked = True  # Se detecta el clic
                    self.sound_click.play()
        else:
            self.pressed = False
            self.hover = False

    def draw(self, display):
        # Definir los colores del botón
        top_rect_color = "#317bcf" if self.hover else "#3194cf"
        bottom_rect_color = "#1a232e"

        # Si no se presiona el botón, dibujar en su posición original
        if not self.pressed:
            pygame.draw.rect(display, bottom_rect_color, self.bottom_rect)
            pygame.draw.rect(display, top_rect_color, self.top_rect)
            self.text_rect.center = self.top_rect.center

            if self.image:
                display.blit(self.image, self.top_rect.topleft)
            else:
                display.blit(self.text, self.text_rect)

        # Si se presiona, el botón "baja" un poco
        else:
            pygame.draw.rect(display, top_rect_color, self.bottom_rect)
            self.text_rect.center = self.bottom_rect.center

            if self.image:
                display.blit(self.image, self.bottom_rect.topleft)
            else:
                display.blit(self.text, self.text_rect)

    def is_clicked(self):
        return self.clicked






class Game:
    def __init__(self, screen, block, nivel):
        self.nivel = nivel
        self.screen = screen
        self.goal_pos = (diccionario[self.nivel]['objetivo'][0], diccionario[self.nivel]['objetivo'][1])
        self.block = block
        self.TILE_SIZE = block.TILE_SIZE
        self.board = np.array(diccionario[self.nivel]['tablero'])
        self.play = False
        self.button_return = Button(screen.get_width() - 100, screen.get_height() - 50,"BACK", 20, 70, 40)  # objeto de la clse Button
        self.background_image = pygame.transform.scale(pygame.image.load(resource_path("Graphics/fondo.png")), (screen.get_width(), screen.get_height()))
        self.direction = DirectionButtons(screen)
        self.block_image = pygame.transform.scale(pygame.image.load(resource_path("Graphics/textura.png")), (self.TILE_SIZE, self.TILE_SIZE))  # Escalar la imagen al tamaño del cuadro
        self.block_X = pygame.transform.scale(pygame.image.load(resource_path("Graphics/textura_X.png")), (self.TILE_SIZE, self.TILE_SIZE))  # Escalar la imagen al tamaño del cuadro
        self.block_O = pygame.transform.scale(pygame.image.load(resource_path("Graphics/textura_o.png")), (self.TILE_SIZE, self.TILE_SIZE))  # Escalar la imagen al tamaño del cuadro
        self.block_D = pygame.transform.scale(pygame.image.load(resource_path("Graphics/textura_d.png")), (self.TILE_SIZE, self.TILE_SIZE))  # Escalar la imagen al tamaño del cuadro
        self.w = (self.screen.get_width() - len(self.board[0]) * self.TILE_SIZE) // 2
        self.h = 50
        self.sound_block = pygame.mixer.Sound(resource_path('Sounds/sound_block.mp3'))
        self.death = pygame.mixer.Sound(resource_path('Sounds/Death.mp3'))
        self.acti = pygame.mixer.Sound(resource_path('Sounds/acti.mp3'))
        self.win = pygame.mixer.Sound(resource_path('Sounds/win.mp3'))
        self.anterior = None

    def reset_game(self):
        self.block.reset_block(self.nivel)
        self.board = np.array(diccionario[self.nivel]['tablero'])
        self.goal_pos = (diccionario[self.nivel]['objetivo'][0], diccionario[self.nivel]['objetivo'][1])


    # Función para verificar si la posición del bloque es válida
    def is_valid_position(self):
        # Obtener todas las posiciones ocupadas por el bloque
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

                if int(self.board[y][x]) == 2:
                    self.board[abs(self.board) == 1+(self.board[y][x]/10)] = -self.board[abs(self.board) == 1+(self.board[y][x]/10)]
                    self.acti.play()

                if int(self.board[y][x]) == 3 and self.block.orientation == 'punto':
                    self.board[abs(self.board) == 1 + (self.board[y][x] / 10)] = -self.board[abs(self.board) == 1 + (self.board[y][x] / 10)]
                    self.acti.play()

                if self.board[y][x] == 4 and self.block.orientation == 'punto':
                    self.board[y][x] = 0
                    return False

                if int(self.board[y][x]) == 5:
                    self.board[abs(self.board) == round(self.board[y][x] - 4, 2)] = -abs(self.board[abs(self.board) == round(self.board[y][x] - 4, 2)])
                    self.acti.play()
            self.anterior = positions
            self.sound_block.play()
        return True

    # Dentro de la función draw_board() o en tu ciclo principal de dibujo
    def draw_board(self):
        self.w = (self.screen.get_width() - len(self.board[0]) * self.TILE_SIZE) // 2
        self.h = 50
        for y, row in enumerate(self.board):
            for x, tile in enumerate(row):
                if int(tile) == 1:  # Si es una casilla válida (suelo)
                    self.screen.blit(self.block_image, (self.w + (x * self.TILE_SIZE), self.h + (y * self.TILE_SIZE)))  # Dibuja la imagen
                elif int(tile) == 2 or int(tile) == 5:
                    self.screen.blit(self.block_O, (self.w + (x * self.TILE_SIZE), self.h + (y * self.TILE_SIZE)))  # Dibuja la imagen
                elif int(tile) == 3:
                    self.screen.blit(self.block_X, (self.w + (x * self.TILE_SIZE), self.h + (y * self.TILE_SIZE)))  # Dibuja la imagen
                elif tile == 4:
                    self.screen.blit(self.block_D, (self.w + (x * self.TILE_SIZE), self.h + (y * self.TILE_SIZE)))  # Dibuja la imagen
                if tile > 0:
                    pygame.draw.rect(self.screen, LIGHT_GRAY, (self.w + (x * self.TILE_SIZE), self.h + (y * self.TILE_SIZE), self.TILE_SIZE, self.TILE_SIZE),1)  # Borde
        pygame.draw.rect(self.screen, RED, (self.w + (self.goal_pos[0] * self.TILE_SIZE), self.h + (self.goal_pos[1] * self.TILE_SIZE), self.TILE_SIZE, self.TILE_SIZE))

    def retornar(self):
        if self.button_return.clicked: # si el boton play es tocado, cambiar menu_finished a True
            return True

    def update(self, event):
        self.direction.position_update()
        self.block.update(event, self.direction.direction)
        self.direction.direction = ""
        self.button_return.update()
        if self.block.jugar:
            self.direction.update()

        # Verificar si la posición es válida después de cada movimiento
        if not self.is_valid_position():
            #print("¡Perdiste!")
            self.death.play()
            self.reset_game()

    def draw(self):
        # Dibujar todo
        self.screen.blit(self.background_image, (0, 0))
        self.draw_board()
        self.button_return.draw(self.screen)
        if self.block.jugar:
            self.direction.draw()
        self.block.draw(self.screen, self.w, self.h)
        # Comprobar si ha llegado al objetivo
        if (self.block.x, self.block.y) == self.goal_pos and self.block.orientation == 'punto':
            #print("¡Has ganado!")
            self.win.play()
            self.nivel += 1
            self.reset_game()
        pygame.display.flip()






# Simular botones de dirección
class DirectionButtons:
    def __init__(self, screen):
        self.screen = screen
        self.button_left = Button(320, screen.get_height() - 70, "<-", 30, 60, 60)  # boton derecha
        self.button_down = Button(400, screen.get_height() - 70, "V", 30, 60, 60)  # boton derecha
        self.button_right = Button(480, screen.get_height() - 70, "->", 30, 60, 60)  # boton derecha
        self.button_up = Button(400, screen.get_height() - 150, "A", 30, 60, 60)  # boton derecha
        self.direction = ''
    def position_update(self):
        if self.button_right.clicked: # si el boton play es tocado, cambiar menu_finished a True
            self.direction = 'right'
        if self.button_left.clicked: # si el boton play es tocado, cambiar menu_finished a True
            self.direction = 'left'
        if self.button_up.clicked: # si el boton play es tocado, cambiar menu_finished a True
            self.direction = 'up'
        if self.button_down.clicked: # si el boton play es tocado, cambiar menu_finished a True
            self.direction = 'down'

    def draw(self):
        self.button_right.draw(self.screen)
        self.button_left.draw(self.screen)
        self.button_down.draw(self.screen)
        self.button_up.draw(self.screen)

    def update(self):
        self.button_right.update()
        self.button_left.update()
        self.button_down.update()
        self.button_up.update()








class Block:
    def __init__(self, x, y, TILE_SIZE):
        # El bloque comienza "de pie"
        self.x = x
        self.y = y
        self.TILE_SIZE = TILE_SIZE
        self.jugar = False
        self.orientation = "punto"  # vertical, horizontal_x, horizontal_y

    def update(self, event, direc):
        if self.jugar:
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT) or direc == 'left':
                    self.move(-1, 0)
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT) or direc == 'right':
                    self.move(1, 0)
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) or direc == 'up':
                    self.move(0, -1)
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN) or direc == 'down':
                    self.move(0, 1)


    def move(self, dx, dy):
        if self.orientation == "vertical":  # Cuando está en posición vertical
            if dx != 0:  # Movimiento horizontal
                self.x += dx  # Mueve dos unidades en esa dirección
                self.orientation = "vertical"
            if dy != 0:  # Movimiento vertical
                self.y += dy if dy < 0 else dy * 2
                self.orientation = "punto"

        elif self.orientation == "punto":  # Cuando está acostado horizontalmente a lo largo del eje x
            if dx != 0:  # Movimiento horizontal
                self.x += dx*2 if dx < 0 else dx
                self.orientation = "horizontal"
            if dy != 0:  # Movimiento vertical
                self.y += dy*2 if dy < 0 else dy
                self.orientation = "vertical"

        elif self.orientation == "horizontal":  # Cuando está acostado horizontalmente a lo largo del eje y
            if dx != 0:  # Movimiento horizontal
                self.x += dx if dx < 0 else dx*2
                self.orientation = "punto"
            if dy != 0:  # Movimiento vertical
                self.y += dy
                self.orientation = "horizontal"

    def get_positions(self):
        """Devuelve una lista con las posiciones ocupadas por el bloque."""
        if self.orientation == "vertical":
            return [(self.x, self.y), (self.x, self.y + 1)]
        elif self.orientation == "horizontal":
            return [(self.x, self.y), (self.x + 1, self.y)]
        else:  # "punto"
            return [(self.x, self.y)]

    def reset_block(self, nivel):
        self.x = diccionario[nivel]['inicial'][0]
        self.y = diccionario[nivel]['inicial'][1]
        self.TILE_SIZE = self.TILE_SIZE
        self.orientation = "punto"  # vertical, horizontal_x, horizontal_y

    def draw(self, screen, w, h):
        if self.orientation == "vertical":  # Dibuja el bloque vertical
            pygame.draw.rect(screen, BLUE, (w + self.x * self.TILE_SIZE, h + self.y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE * 2))
        elif self.orientation == "punto":  # Dibuja el bloque acostado a lo largo del eje x
            pygame.draw.rect(screen, BLUE, (w + self.x * self.TILE_SIZE, h + self.y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE))
        elif self.orientation == "horizontal":  # Dibuja el bloque acostado a lo largo del eje y
            pygame.draw.rect(screen, BLUE, (w + self.x * self.TILE_SIZE, h + self.y * self.TILE_SIZE, self.TILE_SIZE * 2, self.TILE_SIZE))









# Crear ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bloxorz 2D")
# Crear bloque
block = Block(diccionario[nivel]['inicial'][0], diccionario[nivel]['inicial'][1], 40)
game = Game(screen, block, nivel)
menu = Menu(screen)
# Ciclo principal del juego



while True:
    if music_num==0:
        pygame.mixer.music.load(resource_path("Sounds/espera.mp3"))
        pygame.mixer.music.play(-1)
        music_num = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT or menu.exit:
            pygame.quit()
            sys.exit()
        elif not game.play and menu.finished:
            game.update(event)
            if music_num == 1:
                pygame.mixer.music.load(resource_path("Sounds/Bloxorz.mp3"))
                pygame.mixer.music.play(-1)
                music_num = 2
            if game.retornar():
                music_num = 0
                menu.set_menu()
                game.nivel = 1
                game.reset_game()
            game.draw()
    if not menu.finished:
        menu.update()
        menu.draw()
        block.jugar = menu.jugar

    pygame.time.Clock().tick(60)