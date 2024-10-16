import pygame


class Gif:
    """
        Clase para cargar y reproducir una secuencia de imágenes, simulando un GIF animado en Pygame.

        Atributos:
        ----------
        screen : pygame.Surface
            La pantalla donde se renderiza el GIF.

        images : list
            Lista de rutas a las imágenes que componen el GIF.

        current_image : int
            Índice de la imagen que se está mostrando actualmente.

        frame_delay : int
            Tiempo de retraso entre cada frame del GIF en milisegundos.

        image : pygame.Surface
            Superficie de la imagen actual que se está dibujando en la pantalla.

        last_update : int
            Tiempo (en ticks) del último cambio de frame.

        Métodos:
        --------
        draw():
            Dibuja la imagen actual en la pantalla.

        update_image():
            Actualiza la imagen actual del GIF si ha pasado suficiente tiempo desde la última actualización.
    """
    def __init__(self, screen, ruta, similar):
        """
            Inicializa el objeto Gif cargando las imágenes desde la ruta especificada.

            Parámetros:
            -----------
            screen : pygame.Surface
                La pantalla donde se renderizará el GIF.

            ruta : str
                La ruta donde se encuentran las imágenes del GIF.

            similar : str
                Nombre base de los archivos de imagen, se espera que estén numerados consecutivamente.
        """
        self.screen = screen
        self.images = [ruta+"/"+similar+str(i)+".jpg" for i in range(44)]
        self.current_image = 0  # Índice de la imagen actual
        self.frame_delay = 20  # Tiempo entre frames en milisegundos
        print(self.images)
        self.image = pygame.transform.scale(pygame.image.load(self.images[self.current_image]), (screen.get_width(), screen.get_height()))
        self.last_update = pygame.time.get_ticks()

    def draw(self):
        """
            Dibuja la imagen actual del GIF en la pantalla.
        """
        self.screen.blit(self.image, (0, 0))

    def update_image(self):
        """
            Actualiza la imagen actual del GIF si ha pasado suficiente tiempo desde el último frame.
        """
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_delay:
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = pygame.transform.scale(pygame.image.load(self.images[self.current_image]),(self.screen.get_width(), self.screen.get_height()))
            self.last_update = now
    pass
