# Conector base de datos:
import mysql.connector

__conexion = None

def conectar_database():
    global __conexion
    if __conexion is None:
        __conexion = mysql.connector.connect(user="root",
        password = "Gracias_Vuelva_Prontos",
        host = "127.0.0.1",
        database = "kwik_e_mart")
    return __conexion