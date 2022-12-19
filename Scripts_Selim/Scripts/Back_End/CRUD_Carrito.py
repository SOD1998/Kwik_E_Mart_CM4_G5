# CRUD Carrito:
import sys # Paquete usado para invocar a funciones y clases creadas en carpetas diferentes.
sys.path.append(r'F:\Visual Studio Code\Scripts_Selim\Scripts') # Dirección usada por defecto al escribir el código.
from Back_End.CRUD_Producto import consultar_stock
# Agregar al carrito:
def agregar_producto_nuevo(conexion, id_producto, id_usuario, cantidad):
    stock_disp = consultar_stock(conexion, id_producto)
    if (stock_disp >= cantidad):
        cursor = conexion.cursor()
        consulta = ("INSERT into carrito (id_producto, id_usuario, cantidad) VALUES (%s, %s, %s)")
        datos = (id_producto, id_usuario, cantidad)
        cursor.execute(consulta, datos)
        conexion.commit()
        print("Producto agregado al carrito")
    else:
        print("No hay suficiente producto disponible")
# Ver listado:
def ver_listado(conexion, id_usuario): # Listado de compras del usuario.
    cursor = conexion.cursor()
    consulta = ("SELECT producto.nombre, producto.marca, producto.vencimiento, producto.precio, "
    "carrito.cantidad FROM kwik_e_mart.carrito "
    "INNER JOIN producto ON carrito.id_producto = producto.id WHERE id_usuario=" +str(id_usuario))
    cursor.execute(consulta)
    respuesta = []
    for (nombre, marca, vencimiento, precio, cantidad) in cursor:
        respuesta.append((nombre, marca, vencimiento, precio, cantidad))
    return respuesta
# Listado de productos comprados
def ver_prod_comprados(conexion, id_usuario):
    cursor = conexion.cursor()
    consulta = ("SELECT carrito.id_producto, carrito.cantidad FROM kwik_e_mart.carrito "
    "INNER JOIN producto ON carrito.id_producto = producto.id WHERE id_usuario=" +str(id_usuario))
    cursor.execute(consulta)
    respuesta = []
    for (id_producto, cantidad) in cursor:
        respuesta.append((id_producto, cantidad))
    return respuesta
# Calcular el total acumulado:
def total_acum(conexion, id_usuario):
    cursor = conexion.cursor()
    consulta = ("SELECT producto.precio, carrito.cantidad FROM kwik_e_mart.carrito "
    "INNER JOIN producto ON carrito.id_producto = producto.id WHERE id_usuario=" +str(id_usuario))
    cursor.execute(consulta)
    respuesta = []
    total_lista = []
    for (precio, cantidad) in cursor:
        respuesta.append((precio, cantidad))
    for prod in respuesta:
        total_parcial = prod[0]*prod[1]
        total_lista.append(total_parcial)
    total = sum(total_lista)
    return total
# Calcular descuento:
def descuento_acum(conexion, id_usuario):
    total = total_acum(conexion, id_usuario)
    if (total >= 5000):
        descuento = 0.1
    else:
        descuento = 0
    return descuento
# Vaciar carrito:
def vaciar_carrito(conexion, id_usuario):
    cursor = conexion.cursor()
    consulta = ("DELETE FROM kwik_e_mart.carrito WHERE carrito.id_usuario=" + str(id_usuario))
    cursor.execute(consulta)
    conexion.commit()
    return cursor.lastrowid