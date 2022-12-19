# Clase: Carrito
class Carrito:
    def __init__(self, producto, cantidad):
        self.__producto = producto
        self.__cantidad = cantidad
# Mostrar con print
    def __str__(self):
        cadena = str(f"Productos: {self.__producto} \n Cantidad: {self.__cantidad}")
        return cadena
# Getters:
    def get_producto(self):
        producto = self.__producto
        return producto
    def get_cantidad(self):
        cantidad = self.__cantidad
        return cantidad
# Setters:
    def set_producto(self, producto):
        self.__producto = producto
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
