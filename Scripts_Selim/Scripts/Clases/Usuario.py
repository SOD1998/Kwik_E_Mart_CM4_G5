# Clase: Usuario
class Usuario:
# Constructor:
    def __init__(self, nombre, apellido, fecha_nacimiento, email, password, tarjeta, domicilio):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        self.__email = email
        self.__password = password
        self.__tarjeta = tarjeta
        self.__domicilio = domicilio
# Mostrar con print
    def __str__(self):
        cadena = str(f"Apellido y nombre: {self.__apellido} {self.__nombre} \n Fecha de nacimiento: {self.__fecha_nacimiento} \n Correo electrónico: {self.__email} \n Contraseña: {self.__password} \n Datos de tarjeta: {self.__tarjeta} \n Domicilio: {self.__domicilio}")
        return cadena
# Getters:
    def get_nombre(self):
        nombre = self.__nombre
        return nombre
    def get_apellido(self):
        apellido = self.__apellido
        return apellido
    def get_fecha_nacimiento(self):
        fecha_nacimiento = self.__fecha_nacimiento
        return fecha_nacimiento
    def get_email(self):
        email = self.__email
        return email
    def get_password(self):
        password = self.__password
        return password
    def get_tarjeta(self):
        tarjeta = self.__tarjeta
        return tarjeta
    def get_domicilio(self):
        domicilio = self.__domicilio
        return domicilio
# Setters:
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_apellido(self, apellido):
        self.__apellido = apellido
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
    def set_email(self, email):
        self.__email = email
    def set_password(self, password):
        self.__password = password
    def set_tarjeta(self, tarjeta):
        self.__tarjeta = tarjeta
    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio