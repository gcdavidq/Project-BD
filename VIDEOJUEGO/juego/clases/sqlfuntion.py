import pymysql
# Clase para manejar las funciones SQL
class SQLFuntion:
    """
        Clase para manejar las funciones SQL en una base de datos MySQL utilizando pymysql.

        Atributos:
        ----------
        connection : pymysql.connections.Connection
            La conexión a la base de datos MySQL.

        Métodos:
        --------
        obtener_informacion_movimientos():
            Obtiene el último movimiento permitido desde la base de datos.

        actualizar_registro(voto, historial_id, level, orientation, x, y, board):
            Actualiza el registro en la base de datos utilizando un procedimiento almacenado.
    """
    def __init__(self):
        """
            Inicializa la conexión a la base de datos utilizando los parámetros especificados.
        """
        # Parámetros de conexión
        self.connection = pymysql.connect(
            host='autorack.proxy.rlwy.net',
            port=56092,
            user='all_user',
            password='8765',
            database='bd_project'
        )

    # Función para obtener movimientos permitidos desde la base de datos
    def obtener_informacion_movimientos(self):
        """
            Obtiene el último movimiento permitido desde la base de datos.

            Retorna:
            --------
            tuple o None:
                Devuelve una tupla con el último movimiento si se encuentra,
                o None si ocurre un error en la consulta.
        """
        self.connection = pymysql.connect(
            host='autorack.proxy.rlwy.net',
            port=56092,
            user='all_user',
            password='8765',
            database='bd_project'
        )
        try:
            with self.connection.cursor() as cursor:
                cursor.execute('''
                    SELECT id_historial, time_insert, nivel, orientation, posicion_x, posicion_y, board
                    FROM historial
                    ORDER BY id_historial DESC
                    LIMIT 1
                ''')
                movimientos_permitidos = cursor.fetchone()  # Devuelve una tupla
            return movimientos_permitidos
        except pymysql.MySQLError as e:
            #print(f"Error al obtener movimientos: {e}")
            return None

    # Función para actualizar el registro
    def actualizar_registro(self, voto, historial_id, level, orientation, x, y, board):
        """
            Actualiza el registro en la base de datos utilizando un procedimiento almacenado.

            Parámetros:
            -----------
            voto : int
                El voto que se desea registrar.

            historial_id : int
                El ID del historial que se está actualizando.

            level : int
                El nivel relacionado con el registro.

            orientation : str
                La orientación del movimiento.

            x : int
                La posición X del movimiento.

            y : int
                La posición Y del movimiento.

            board : str
                El estado del tablero.

            Retorna:
            --------
            None:
                No devuelve nada. Si ocurre un error, se ignora.
            """
        try:
            with self.connection.cursor() as cursor:
                # Llamar a un procedimiento almacenado
                cursor.callproc('registrar_voto', (voto, historial_id, level, orientation, x, y, board))
                self.connection.commit()
        except pymysql.MySQLError as e:
            #print(f"Error al actualizar registro: {e}")
            pass
    pass