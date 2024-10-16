import pygame
from clases.button import Button
from clases.gif import Gif
from clases.nombre import TextInputBox

class NameInputScreen:
    """
        Clase que representa la pantalla de entrada de nombre en el juego.

        Atributos:
        ----------
        screen : pygame.Surface
            La superficie de Pygame donde se dibujarán los elementos de la pantalla.
        input_box : TextInputBox
            Objeto que permite la entrada de texto para el nombre del jugador.
        button_listo : Button
            Botón que indica que el usuario ha terminado de ingresar su nombre.
        finished : bool
            Indica si se ha completado la entrada del nombre.
        name : str
            Almacena el nombre ingresado por el usuario.
        welcome_screen : Gif
            Objeto que representa la animación de fondo de bienvenida.
        block_title : pygame.Surface
            Imagen que se mostrará como título en la pantalla.

        Métodos:
        --------
        update(event):
            Maneja los eventos de entrada, actualiza el estado de la pantalla y verifica la entrada del nombre.

        update_image():
            Actualiza la imagen de fondo de bienvenida.

        draw():
            Dibuja todos los elementos en la pantalla.
    """
    def __init__(self, screen):
        """
            Inicializa la pantalla de entrada de nombre y sus elementos gráficos.

            Parámetros:
            -----------
            screen : pygame.Surface
                La superficie de Pygame donde se dibujarán los elementos de la pantalla.
        """
        self.screen = screen
        self.input_box = TextInputBox((screen.get_width() // 2) - 100, screen.get_height() // 2, 200, 32)
        self.button_listo = Button((screen.get_width() // 2) - 100, screen.get_height() // 2 + 70, "LISTO", text_color="#27afe3")
        self.finished = False
        self.name = ''
        self.welcome_screen = Gif(self.screen, 'Graphics', 'fondo-00')
        self.block_title = pygame.transform.scale(pygame.image.load("Graphics/blo.png"),(screen.get_width() - 200, screen.get_height() - 500))

    def update(self, event):
        """
            Maneja los eventos de entrada y actualiza el estado de la pantalla.

            Parámetros:
            -----------
            event : pygame.event.Event
                El evento que se está manejando. Puede ser un clic del ratón o una pulsación de tecla.
        """
        self.input_box.handle_event(event)
        self.button_listo.update()

        if self.button_listo.clicked and self.input_box.text != '':  # Cuando se presiona el botón "LISTO"
            self.name = self.input_box.text
            self.finished = True

    def update_image(self):
        """
            Actualiza la imagen de fondo de bienvenida.
        """
        self.welcome_screen.update_image()

    def draw(self):
        """
            Dibuja todos los elementos de la pantalla.

            Dibuja la imagen de fondo, el título, la caja de entrada y el botón en la superficie de Pygame.
        """
        self.welcome_screen.draw()
        self.screen.blit(self.block_title, (100, 100))
        self.input_box.draw(self.screen)
        self.button_listo.draw(self.screen)
        pygame.display.flip()
    pass