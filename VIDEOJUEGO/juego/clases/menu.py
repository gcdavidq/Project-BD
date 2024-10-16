import pygame
from clases.button import Button
from clases.gif import Gif

class Menu:
    """
        Clase que representa el menú principal del juego, con un GIF de fondo y botones para interactuar.

        Atributos:
        ----------
        screen : pygame.Surface
            La pantalla donde se renderiza el menú.

        welcome_screen : Gif
            Animación de fondo que se muestra en el menú, simulando un GIF.

        block_title : pygame.Surface
            Imagen estática que se muestra en la parte superior del menú (probablemente un logo o título).

        finished : bool
            Estado que indica si el usuario ha terminado de interactuar con el menú.

        play : bool
            Indica si el usuario ha seleccionado la opción de jugar.

        button_play : Button
            Botón que, al ser presionado, lleva al juego.

        button_ver : Button
            Botón que, al ser presionado, activa una función alternativa (como ver algo adicional).

        Métodos:
        --------
        set_menu():
            Restablece el menú a su estado inicial, marcando `finished` como False.

        update():
            Actualiza el estado de los botones y la animación de fondo.

        draw():
            Dibuja la animación de fondo, el título y los botones en la pantalla.
    """
    def __init__(self, screen):
        """
            Inicializa el menú con una pantalla, un GIF de fondo y dos botones (Jugar y Ver).

            Parámetros:
            -----------
            screen : pygame.Surface
                La pantalla en la que se renderizará el menú.
        """
        self.screen = screen
        self.welcome_screen = Gif(self.screen, 'Graphics', 'fondo-00')
        self.block_title = pygame.transform.scale(pygame.image.load("Graphics/blo.png"), (screen.get_width()-200, screen.get_height()-500))
        self.finished= False
        self.play = False
        self.button_play = Button((screen.get_width() // 2)-100, screen.get_height() // 2, "JUGAR")  # objeto de la clse Button
        self.button_ver = Button((screen.get_width() // 2) - 100, screen.get_height() // 2 + 70,"VER")  # objeto de la clse Button

    def set_menu(self):
        """
            Reinicia el estado del menú, marcándolo como no terminado (`finished = False`).
        """
        self.finished = False

    def update(self):
        """
            Actualiza el estado del menú verificando si se han presionado los botones y actualizando el GIF de fondo.
            Cambia el estado a `finished = True` si el botón 'JUGAR' o 'VER' son presionados.
        """
        if self.button_play.clicked: # si el boton play es tocado, cambiar finished a True
            self.finished = True
            self.play = True
        if self.button_ver.clicked: # si el boton play es tocado, cambiar finished a True
            self.finished = True
            self.play = False
        self.welcome_screen.update_image()
        self.button_play.update()
        self.button_ver.update()

    def draw(self):
        """
            Dibuja el menú en la pantalla: fondo animado, título y botones.
        """
        self.welcome_screen.draw()
        self.screen.blit(self.block_title, (100, 100))
        self.button_play.draw(self.screen)
        self.button_ver.draw(self.screen)
        pygame.display.flip()
    pass
