# Clase: Producto
class Producto:
    def __init__(self, id, nombre, marca, vencimiento, stock, precio):
        self.__id = id
        self.__nombre = nombre
        self.__marca = marca
        self.__vencimiento = vencimiento
        self.__precio = precio
        self.__stock = stock
# Mostrar con print
    def __str__(self):
        cadena = str(f"Nombre: {self.__nombre} \n Marca: {self.__marca} \n Vencimiento: {self.__vencimiento} \n Precio: ${self.__precio} \n Stock: {self.__stock}")
        return cadena
# Getters:
    def get_nombre(self):
        nombre = self.__nombre
        return nombre
    def get_id(self):
        id = self.__id
        return id
    def get_marca(self):
        marca = self.__marca
        return marca
    def get_vencimiento(self):
        vencimiento = self.__vencimiento
        return vencimiento
    def get_precio(self):
        precio = self.__precio
        return precio
    def get_stock(self):
        stock = self.__stock
        return stock
# Setters:
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_id(self, id):
        self.__id = id
    def set_marca(self, marca):
        self.__marca = marca
    def set_vencimiento(self, vencimiento):
        self.__vencimiento = vencimiento
    def set_precio(self, precio):
        self.__precio = precio
    def set_stock(self, stock):
        self.__stock = stock
# Agregar producto:
    def agregar(self, cantidad):
        if (not type(cantidad) is int):
            raise TypeError("Solo se pueden agregar cantidades enteras")
        elif (cantidad <= 0):
            raise Exception("No es posible agregar una cantidad menor o igual que 0")
        else:
            self.__stock = self.__stock + cantidad


