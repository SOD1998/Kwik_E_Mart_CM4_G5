# CRUD Producto:
# Insertar producto nuevo:
def agregar_producto_nuevo(conexion, nombre, marca, vencimiento, stock, precio):
    cursor = conexion.cursor()
    consulta = ("INSERT into producto (nombre, marca, vencimiento, stock, precio) VALUES (%s, %s, %s, %s, %s)")
    datos = (nombre, marca, vencimiento, stock, precio)
    cursor.execute(consulta, datos)
    conexion.commit()
    print("Producto agregado")
# Modificar producto existente:
def modificar_producto(conexion, id, nombre, marca, vencimiento, stock, precio):
    cursor = conexion.cursor()
    consulta = ("UPDATE producto SET producto.nombre = %s, producto.marca = %s, "
    "producto.vencimiento = %s, producto.stock = %s, producto.precio = %s WHERE producto.id = %s")
    datos = (nombre, marca, vencimiento, stock, precio, id)
    cursor.execute(consulta, datos)
    conexion.commit()
    print("Producto actualizado exitosamente")
def actualizar_stock(conexion, id_producto, cantidad):
    cursor = conexion.cursor()
    consulta = ("UPDATE producto SET producto.stock = %s WHERE producto.id = %s")
    datos = (cantidad, id_producto)
    cursor.execute(consulta, datos)
    conexion.commit()
    print("Stock actualizado")

# Eliminar producto existente:
def eliminar_producto(conexion, id_producto):
    cursor = conexion.cursor()
    consulta = ("DELETE FROM kwik_e_mart.producto where id=" + str(id_producto))
    cursor.execute(consulta)
    conexion.commit()
    return cursor.lastrowid

# Buscar producto en base de datos:
def buscar_todos_productos(conexion): # Busca a todos los productos disponibles.
    cursor = conexion.cursor()
    consulta = ("SELECT producto.nombre, producto.marca, producto.vencimiento, "
    "producto.stock, producto.precio FROM kwik_e_mart.producto")
    cursor.execute(consulta)
    respuesta = []
    for (nombre, marca, vencimiento, stock, precio) in cursor:
        respuesta.append((nombre, marca, vencimiento, stock, precio))
    return respuesta

def buscar_producto_nombre(conexion, nombre_producto): # Busca prodcutos por su nombre.
    cursor = conexion.cursor()
    consulta = ("SELECT producto.nombre, producto.marca, producto.vencimiento, "
    "producto.stock, producto.precio FROM kwik_e_mart.producto WHERE nombre = '" + nombre_producto + "'")
    cursor.execute(consulta)
    respuesta = []
    for (nombre, marca, vencimiento, stock, precio) in cursor:
        respuesta.append((nombre, marca, vencimiento, stock, precio))
    return respuesta

def consultar_stock(conexion, id_producto): # Consulta el stock de un producto en particular.
    cursor = conexion.cursor()
    consulta = ("SELECT producto.stock FROM kwik_e_mart.producto WHERE id="+ str(id_producto))
    cursor.execute(consulta)
    respuesta = []
    for (stock) in cursor:
        respuesta.append(stock)
    resultado = sum(respuesta[0])
    return resultado