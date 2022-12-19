# Clase: Comprobante
class Comprobante:
    def __init__(self, cliente, detalle, iva, total, descuento, forma_pago):
        self.__cliente = cliente
        self.__detalle = detalle
        self.__iva = iva
        self.__total = total
        self.__descuento = descuento
        self.__forma_pago = forma_pago
# Mostrar con print
    def __str__(self):
        cadena = str(f"Cliente: {self.__cliente} \n Detalle: {self.__detalle} \n IVA: {self.__iva} \n Descuento: {self.__descuento} \n Total: {self.__total} \n Método de pago: {self.__forma_pago}")
        return cadena
# Getters:
    def get_cliente(self):
        cliente = self.__cliente
        return cliente
    def get_detalle(self):
        detalle = self.__detalle
        return detalle
    def get_iva(self):
        iva = self.__iva
        return iva
    def get_total(self):
        total = self.__total
        return total
    def get_descuento(self):
        descuento = self.__descuento
        return descuento
    def get_forma_pago(self):
        forma_pago = self.__forma_pago
        return forma_pago
# Setters:
    def set_cliente(self, cliente):
        self.__cliente = cliente
    def set_detalle(self, detalle):
        self.__detalle = detalle
    def set_iva(self, iva):
        self.__iva = iva
    def set_total(self, total):
        self.__total = total
    def set_descuento(self, descuento):
        self.__descuento = descuento
    def set_forma_pago(self, forma_pago):
        self.__forma_pago = forma_pago