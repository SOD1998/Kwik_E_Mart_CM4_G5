# CRUD clase Usuario:
# Iniciar sesión:
def iniciar_sesion(conexion, email_usuario, clave_usuario):
    cursor = conexion.cursor()
    consulta = ("SELECT usuario.email, usuario.clave, usuario.rol "
    "FROM kwik_e_mart.usuario WHERE email = '" + email_usuario + "'")
    cursor.execute(consulta)
    for (email, clave, rol) in cursor:
        if ((email == email_usuario) & (clave == clave_usuario) & (rol == 1)):
            return 1
        elif ((email == email_usuario) & (clave == clave_usuario) & (rol == 0)):
            return 0
        else:
            return -1
# Registrarse:
def registar_cliente(conexion, nombre, apellido, email, clave, nacimiento):
    cursor = conexion.cursor()
    consulta = ("INSERT into usuario (nombre, apellido, email, clave, fecha_de_nacimiento) "
    "VALUES (%s, %s, %s, %s, %s)")
    datos = (nombre, apellido, email, clave, nacimiento)
    cursor.execute(consulta, datos)
    conexion.commit()
# Eliminar cuenta:
def eliminar_cuenta(conexion, usuario_id):
    cursor = conexion.cursor()
    consulta = ("DELETE FROM kwik_e_mart.usuario where id=" + str(usuario_id))
    cursor.execute(consulta)
    conexion.commit()
    print("Cuenta eliminada")
    return cursor.lastrowid
# Lista de usuarios:
def buscar_todos_usuarios(conexion):
    cursor = conexion.cursor()
    consulta = ("SELECT usuario.nombre, usuario.apellido, usuario.email, usuario.fecha_de_nacimiento, "
    "domicilio.localidad, domicilio.barrio, domicilio.calle FROM kwik_e_mart.usuario "
    "INNER JOIN domicilio ON usuario.id_domicilio = domicilio.id")
    cursor.execute(consulta)
    respuesta = []
    for (nombre, apellido, email, nacimiento, localidad, barrio, calle) in cursor:
        respuesta.append((nombre, apellido, nacimiento, email, localidad, barrio, calle))
    return respuesta
# Actualizar datos de usuario:
def modificar_datos_cuenta(conexion, id, nombre, apellido, email, clave, nacimiento):
    cursor = conexion.cursor()
    consulta = ("UPDATE producto SET usuario.nombre = %s, usuario.apellido = %s, "
    "usuario.email = %s, usuario.clave = %s, usuario.nacimiento = %s WHERE usuario.id = %s")
    datos = (nombre, apellido, email, clave, nacimiento, id)
    cursor.execute(consulta, datos)
    conexion.commit()
    print("Datos actualizados exitosamente")