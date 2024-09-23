# database.py
import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="autorack.proxy.rlwy.net",  # O el host de Railway si lo tienes en la nube
        user="root",
        password="JsOUbxnyMahITwuTxLVVsttChTqjfLHI",
        database="votacion_space_invaders"
    )

def insertar_voto(jugador_id, movimiento):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.callproc('InsertarVoto', (jugador_id, movimiento))
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_movimiento_ganador():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.callproc('ContarVotos')
    cursor.execute("SELECT movimiento FROM movimientos ORDER BY id DESC LIMIT 1")
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()
    return resultado[0] if resultado else None