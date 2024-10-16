import pygame
from clases.dicc import diccionario

class Block:
    """
        Clase que representa el bloque controlado por el jugador en el juego.

        Atributos:
        ----------
        x : int
            La posición inicial en el eje X del bloque.
        y : int
            La posición inicial en el eje Y del bloque.
        TILE_SIZE : int
            El tamaño de cada casilla en el tablero.
        orientation : str
            La orientación actual del bloque ('vertical', 'horizontal', 'punto').
        orientation_prue : str
            La orientación futura del bloque utilizada para verificar colisiones.
        voto : str
            Indica la dirección del movimiento que el bloque ha realizado.
        play : bool
            Indica si el bloque está activo para ser controlado.
        active : bool
            Indica si el bloque está en movimiento.
        x_pru : int
            Posición futura en el eje X del bloque.
        y_pru : int
            Posición futura en el eje Y del bloque.

        Métodos:
        --------
        __init__(x, y, TILE_SIZE, orientation='punto'):
            Inicializa el bloque en una posición específica con un tamaño determinado.

        update(direc):
            Actualiza la posición del bloque en base a las teclas presionadas o la dirección proporcionada.

        move(dx, dy):
            Mueve el bloque una cantidad especificada en los ejes X e Y, ajustando su orientación.

        get_positions():
            Devuelve una lista con las posiciones ocupadas por el bloque, considerando su orientación.

        reset_block(level):
            Reinicia el bloque a su posición inicial para el nivel actual.

        draw(screen, w, h):
            Dibuja el bloque en la pantalla de acuerdo a su posición y orientación actuales.
    """
    def __init__(self, x, y, TILE_SIZE, orientation='punto'):
        """
            Inicializa el bloque en una posición específica con un tamaño determinado.

            Parámetros:
            -----------
            x : int
                Posición inicial en el eje X del bloque.
            y : int
                Posición inicial en el eje Y del bloque.
            TILE_SIZE : int
                Tamaño de cada casilla en el tablero.
            orientation : str, opcional
                Orientación inicial del bloque, por defecto 'punto'.
        """
        self.x = x
        self.y = y
        self.x_pru = x
        self.y_pru = y
        self.voto = '5'
        self.TILE_SIZE = TILE_SIZE
        self.play = False
        self.active = False
        self.orientation = orientation  # vertical, horizontal, punto
        self.orientation_prue = orientation

    def update(self, direc):
        """
            Actualiza la posición del bloque según las teclas presionadas o la dirección proporcionada.

            Si el bloque está activo (`self.play`), captura los eventos de teclado para mover el bloque.
            Si se proporciona un argumento `direc`, mueve el bloque en la dirección especificada ('left', 'right', 'up', 'down').

            Parámetros:
            -----------
            direc : str
                Dirección de movimiento opcional para el bloque ('left', 'right', 'up', 'down').
        """
        if self.play:
            # Capturar todos los eventos dentro de la función
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move(-1, 0)
                        self.voto = '4'
                    elif event.key == pygame.K_RIGHT:
                        self.move(1, 0)
                        self.voto = '3'
                    elif event.key == pygame.K_UP:
                        self.move(0, -1)
                        self.voto = '1'
                    elif event.key == pygame.K_DOWN:
                        self.move(0, 1)
                        self.voto = '2'

            # Control basado en la variable 'direc', si se proporciona
            if direc == 'left':
                self.move(-1, 0)
                self.voto = '4'
            elif direc == 'right':
                self.move(1, 0)
                self.voto = '3'
            elif direc == 'up':
                self.move(0, -1)
                self.voto = '1'
            elif direc == 'down':
                self.move(0, 1)
                self.voto = '2'


    def move(self, dx, dy):
        """
            Mueve el bloque una cantidad especificada en los ejes X e Y, ajustando su orientación.

            Dependiendo de la orientación actual del bloque ('vertical', 'horizontal', 'punto'),
            la función actualiza su posición y cambia la orientación en función del movimiento.

            Parámetros:
            -----------
            dx : int
                Cantidad de desplazamiento en el eje X.
            dy : int
                Cantidad de desplazamiento en el eje Y.
        """
        if self.orientation == "vertical":  # cuando esta acostado a lo largo del eje y
            if dx != 0:  # Movimiento horizontal
                self.x_pru += dx  # Mueve dos unidades en esa dirección
                self.orientation_prue = "vertical"
            if dy != 0:  # Movimiento vertical
                self.y_pru += dy if dy < 0 else dy * 2
                self.orientation_prue = "punto"

        elif self.orientation == "punto":  # Cuando esta parado
            if dx != 0:  # Movimiento horizontal
                self.x_pru += dx*2 if dx < 0 else dx
                self.orientation_prue = "horizontal"
            if dy != 0:  # Movimiento vertical
                self.y_pru += dy*2 if dy < 0 else dy
                self.orientation_prue = "vertical"

        elif self.orientation == "horizontal":  # Cuando está acostado horizontalmente a lo largo del eje x
            if dx != 0:  # Movimiento horizontal
                self.x_pru += dx if dx < 0 else dx*2
                self.orientation_prue = "punto"
            if dy != 0:  # Movimiento vertical
                self.y_pru += dy
                self.orientation_prue = "horizontal"

    def get_positions(self):
        """
            Devuelve una lista con las posiciones ocupadas por el bloque.

            Dependiendo de la orientación actual del bloque, se devuelve una lista
            con una o dos posiciones que el bloque ocupa en el tablero.

            Devuelve:
            ---------
            list of tuple:
                Lista con las coordenadas (x, y) que ocupa el bloque.
        """
        if self.orientation_prue == "vertical":
            return [(self.x_pru, self.y_pru), (self.x_pru, self.y_pru + 1)]
        elif self.orientation_prue == "horizontal":
            return [(self.x_pru, self.y_pru), (self.x_pru + 1, self.y_pru)]
        else:  # "punto"
            return [(self.x_pru, self.y_pru)]

    def reset_block(self, level):
        """
            Reinicia el bloque a su posición inicial para el nivel especificado.

            El bloque es reposicionado de acuerdo a los datos del nivel en el diccionario,
            y su orientación se restablece a 'punto'.

            Parámetros:
            -----------
            level : int
               Nivel actual para reiniciar el bloque.
        """
        self.x_pru = diccionario[level]['inicial'][0]
        self.y_pru = diccionario[level]['inicial'][1]
        self.TILE_SIZE = self.TILE_SIZE
        self.orientation_prue = "punto"

    def draw(self, screen, w, h):
        """
            Dibuja el bloque en la pantalla de acuerdo a su posición y orientación actuales.

            Dependiendo de su orientación ('vertical', 'horizontal', 'punto'), el bloque se dibuja en
            diferentes configuraciones en la superficie de Pygame.

            Parámetros:
            -----------
            screen : pygame.Surface
                Superficie de Pygame donde se dibuja el bloque.
            w : int
                Posición horizontal de referencia para el bloque.
            h : int
                Posición vertical de referencia para el bloque.
        """
        if self.orientation == "vertical":  # Dibuja el bloque acostado a lo largo del eje y
            pygame.draw.rect(screen, (0, 0, 255), (w + self.x * self.TILE_SIZE, h + self.y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE * 2))
        elif self.orientation == "punto":  # Dibuja el bloque parado
            pygame.draw.rect(screen, (0, 0, 255), (w + self.x * self.TILE_SIZE, h + self.y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE))
        elif self.orientation == "horizontal":  # Dibuja el bloque acostado a lo largo del eje x
            pygame.draw.rect(screen, (0, 0, 255), (w + self.x * self.TILE_SIZE, h + self.y * self.TILE_SIZE, self.TILE_SIZE * 2, self.TILE_SIZE))
    pass