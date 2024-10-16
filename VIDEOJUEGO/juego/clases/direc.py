from clases.button import Button

# Simular botones de dirección
class DirectionButtons:
    """
        Simula un conjunto de botones de dirección en la pantalla del juego.

        Atributos:
        ----------
        screen : pygame.Surface
            La pantalla del juego donde se dibujan los botones.

        button_left, button_down, button_right, button_up : Button
            Objetos que representan los botones de dirección (izquierda, abajo, derecha, arriba).

        direction : str
            Una cadena que indica la dirección que se ha seleccionado ('left', 'right', 'up', 'down').

        Métodos:
        --------
        position_update():
            Actualiza la dirección actual en función del botón que ha sido presionado.

        draw():
            Dibuja los botones en la pantalla del juego.

        update():
            Actualiza el estado de los botones (detecta clics o eventos).
    """

    def __init__(self, screen):
        """
            Inicializa los botones de dirección en la pantalla.

            Parámetros:
            -----------
            screen : pygame.Surface
                La pantalla donde se dibujarán los botones.
        """
        self.screen = screen
        self.button_left = Button(320, screen.get_height() - 70, "<-", 30, 60, 60)  # boton derecha
        self.button_down = Button(400, screen.get_height() - 70, "V", 30, 60, 60)  # boton abajo
        self.button_right = Button(480, screen.get_height() - 70, "->", 30, 60, 60)  # boton derecha
        self.button_up = Button(400, screen.get_height() - 150, "A", 30, 60, 60)  # boton arriba
        self.direction = ''
    def position_update(self):
        """
            Actualiza la dirección en función del botón que ha sido presionado.

            Si se detecta que un botón ha sido clicado, la dirección correspondiente
            se asigna a la variable `direction`.
        """
        if self.button_right.clicked: # si el button_right es tocado, cambiar direction a 'right'
            self.direction = 'right'
        if self.button_left.clicked: # si el button_left es tocado, cambiar direction a 'left'
            self.direction = 'left'
        if self.button_up.clicked: # si el button_up es tocado, cambiar direction a 'up'
            self.direction = 'up'
        if self.button_down.clicked: # si el button_down es tocado, cambiar direction a 'down'
            self.direction = 'down'

    def draw(self):
        """
            Dibuja los botones de dirección en la pantalla.
        """
        self.button_right.draw(self.screen)
        self.button_left.draw(self.screen)
        self.button_down.draw(self.screen)
        self.button_up.draw(self.screen)

    def update(self):
        """
            Actualiza el estado de cada botón, verificando si han sido clicados.
        """
        self.button_right.update()
        self.button_left.update()
        self.button_down.update()
        self.button_up.update()
    pass
