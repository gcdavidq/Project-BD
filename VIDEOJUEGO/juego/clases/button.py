import pygame

# Clase modificada del botón
class Button:
    """
        Clase que representa un botón interactivo en la pantalla del juego.

        Atributos:
        ----------
        font : pygame.font.Font
            Fuente utilizada para el texto del botón.
        text : pygame.Surface
            Superficie renderizada con el texto del botón.
        text_rect : pygame.Rect
            Rectángulo que delimita el área del texto.
        image : pygame.Surface or None
            Imagen opcional que puede mostrarse dentro del botón.
        bottom_rect : pygame.Rect
            Rectángulo inferior que se utiliza para crear un efecto de elevación.
        top_rect : pygame.Rect
            Rectángulo superior que representa el área principal del botón.
        hover : bool
            Indica si el ratón está sobre el botón.
        pressed : bool
            Indica si el botón está siendo presionado.
        clicked : bool
            Indica si el botón fue clicado (se liberó después de ser presionado).
        sound_click : pygame.mixer.Sound
            Sonido que se reproduce al hacer clic en el botón.

        Métodos:
        --------
        __init__(x=0, y=0, text="", size=24, width=200, height=50, image=None, elev=6, text_color="#ffffff"):
            Inicializa el botón con las coordenadas, tamaño, imagen y otros parámetros.

        update():
            Actualiza el estado del botón detectando la posición del ratón y si ha sido presionado o clicado.

        draw(display):
            Dibuja el botón en la pantalla. Muestra el botón elevado o presionado dependiendo del estado.

        is_clicked():
            Retorna `True` si el botón ha sido clicado.
    """
    def __init__(self, x=0, y=0, text="", size=24, width=200, height=50, image=None, elev=6, text_color = "#ffffff"):
        """
            Inicializa el botón con las coordenadas, tamaño, imagen y otros parámetros.

            Parámetros:
            -----------
            x : int, opcional
                Coordenada X del botón en la pantalla, por defecto 0.
            y : int, opcional
                Coordenada Y del botón en la pantalla, por defecto 0.
            text : str, opcional
                Texto que se mostrará dentro del botón, por defecto "".
            size : int, opcional
                Tamaño de la fuente del texto, por defecto 24.
            width : int, opcional
                Ancho del botón, por defecto 200.
            height : int, opcional
                Altura del botón, por defecto 50.
            image : pygame.Surface or None, opcional
                Imagen que se mostrará dentro del botón (si se proporciona), por defecto None.
            elev : int, opcional
                Elevación del botón para crear un efecto 3D, por defecto 6.
            text_color : str, opcional
                Color del texto en formato hexadecimal, por defecto "#ffffff".
        """
        self.font = pygame.font.Font('fonts/04B03.ttf', size)
        self.text = self.font.render(text, True, text_color)
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
        self.sound_click = pygame.mixer.Sound('Sounds/click.ogg')

    def update(self):
        """
            Actualiza el estado del botón detectando la posición del ratón y si ha sido presionado o clicado.

            Si el ratón está sobre el botón (`hover`), y se hace clic (se presiona y luego se suelta),
            se activa el sonido y se marca como `clicked`.
        """
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
        """
            Dibuja el botón en la pantalla.

            Si el ratón está sobre el botón, cambia el color del fondo y del borde.
            Si se presiona, el botón "baja" para simular un clic.

            Parámetros:
            -----------
            display : pygame.Surface
                Superficie de Pygame donde se dibuja el botón.
        """
        # Definir los colores del botón: negro de fondo y verde neón en el borde
        top_rect_color = "#27afe3" if self.hover else "#000000"  # Fondo
        border_color = "#000000" if self.hover else "#27afe3"  # Borde verde neón

        # Si no se presiona el botón, dibujar en su posición original
        if not self.pressed:
            pygame.draw.rect(display, border_color, self.bottom_rect)  # Borde
            pygame.draw.rect(display, top_rect_color, self.top_rect)  # Fondo del botón
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
        """
            Verifica si el botón ha sido clicado.

            Devuelve:
            ---------
            bool:
                `True` si el botón fue clicado (presionado y luego soltado), `False` en caso contrario.
        """
        return self.clicked
    pass
