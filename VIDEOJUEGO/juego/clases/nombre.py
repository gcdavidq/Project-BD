import pygame

class TextInputBox:
    """
        Clase que representa una caja de entrada de texto interactiva para recibir texto del usuario.

        Atributos:
        ----------
        rect : pygame.Rect
            El área rectangular donde se renderiza la caja de texto.

        color_inactive : tuple
            El color de la caja cuando no está activa (sin enfoque).

        color_active : tuple
            El color de la caja cuando está activa (con enfoque).

        color : tuple
            El color actual de la caja, que cambia según su estado (activa/inactiva).

        text : str
            El texto ingresado actualmente en la caja.

        txt_surface : pygame.Surface
            La superficie donde se renderiza el texto dentro de la caja.

        active : bool
            Indica si la caja está activa y lista para recibir entrada del teclado.

        Métodos:
        --------
        handle_event(event):
            Maneja los eventos de Pygame relacionados con la entrada del ratón y el teclado.
            - Cambia el estado activo al hacer clic en la caja.
            - Permite ingresar texto si la caja está activa.
            - Devuelve el texto ingresado al presionar Enter.

        draw(screen):
            Dibuja la caja de texto en la pantalla y el texto ingresado en su interior.
    """
    def __init__(self, x, y, w, h, text=''):
        """
            Inicializa la caja de texto con las coordenadas, dimensiones y texto inicial.

            Parámetros:
            -----------
            x : int
                La coordenada X de la esquina superior izquierda de la caja.

            y : int
                La coordenada Y de la esquina superior izquierda de la caja.

            w : int
                El ancho de la caja de texto.

            h : int
                La altura de la caja de texto.

            text : str, opcional
                El texto inicial dentro de la caja (por defecto es una cadena vacía).
        """
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = (39, 176, 147)
        self.color_active = (255, 255, 255)
        self.color = self.color_inactive
        self.text = text
        self.txt_surface = pygame.font.Font(None, 32).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """
            Maneja los eventos relacionados con el ratón y el teclado.

            Parámetros:
            -----------
            event : pygame.event.Event
                El evento de Pygame que debe ser procesado.

            Funcionalidad:
            --------------
            - Si se hace clic dentro de la caja de texto, cambia el estado de activo/inactivo.
            - Si la caja está activa, permite la entrada de texto mediante el teclado.
            - Permite borrar texto con la tecla Backspace y devolver el texto completo con Enter.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text  # Devuelve el texto ingresado
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = pygame.font.Font(None, 32).render(self.text, True, self.color)

    def draw(self, screen):
        """
            Dibuja la caja de texto en la pantalla junto con el texto ingresado.

            Parámetros:
            -----------
            screen : pygame.Surface
                La superficie de Pygame donde se dibuja la caja de texto.
        """
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
    pass

