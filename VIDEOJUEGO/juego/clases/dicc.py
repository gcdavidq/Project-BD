"""
    Diccionario que representa varios niveles de un juego.

    Cada clave (un número entero) representa un nivel diferente. Los valores son diccionarios que contienen la información de cada nivel, la cual incluye:

    Claves de los niveles:
    ----------------------
    'inicial' : tuple(int, int)
        La posición inicial del jugador dentro del tablero, representada como coordenadas (fila, columna).

    'tablero' : list of list
        Representa el tablero de juego, una matriz en la que cada valor tiene un significado especial:
        - 0: Casilla vacía o no navegable.
        - 1: Casilla navegable o transitable.
        - Números negativos: Trampillas vinculadas a los numeros decimales.
        - Números decimales: Puntos especiales con interacción (ej. 2.1, -1.21).

    'objetivo' : tuple(int, int)
        La posición objetivo dentro del tablero, a donde el jugador debe llegar para completar el nivel, representada como coordenadas (fila, columna).

    Ejemplo de nivel:
    -----------------
    Nivel 1:
        'inicial': (1, 1),
        'tablero': [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]],
        'objetivo': (7, 4)

    Descripción de valores:
    -----------------------
    inicial : tuple(int, int)
        La posición inicial del jugador es (1, 1), es decir, la segunda fila y la segunda columna del tablero.

    tablero : list of list
        El tablero de juego es una matriz donde las casillas con valor 1 son transitables y las que tienen 0 no lo son.

    objetivo : tuple(int, int)
        El objetivo del nivel es llegar a la posición (7, 4), es decir, la octava fila y la quinta columna del tablero.
"""
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
                             [0, 1, 1, -1.31, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
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