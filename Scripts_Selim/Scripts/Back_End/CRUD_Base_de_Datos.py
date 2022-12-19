import sys # Paquete usado para invocar a funciones y clases creadas en carpetas diferentes.
sys.path.append(r'F:/Visual Studio Code/Scripts_Selim/Scripts') # Dirección usada por defecto al escribir el código.
from Back_End.Conector import *
# Creador de base de datos:
def crear_base_datos():
    mi_conexion = conectar_database()
    cursor_tablas = mi_conexion.cursor()
    cursor_tablas.execute("create table if not exists administradores "
    "(id int primary key not null,"
    "usuario varchar(20),"
    "clave varchar(50))")
    cursor_tablas.execute("create table if not exists clientes "
    "(cliente_id int primary key not null,"
    "usuario varchar(20),"
    "clave varchar(50),"
    "nombre_cliente varchar(300),"
    "celular varchar(10),"
    "domicilio varchar(300),"
    "DNI varchar(12))")
    cursor_tablas.execute("create table if not exists facturas "
    "(num_factura int primary key not null,"
    "fecha varchar(10),"
    "nombre_cliente varchar(300),"
    "celular_cliente varchar(10))")
    cursor_tablas.execute("create table if not exists productos "
    "(producto_id int primary key not null,"
    "clase varchar(300),"
    "marca varchar(300),"
    "nombre_producto varchar(300),"
    "stock int,"
    "precio_unitario float)")