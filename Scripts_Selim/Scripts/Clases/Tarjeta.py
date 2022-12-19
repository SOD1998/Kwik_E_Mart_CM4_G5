# Clase: Tarjeta
class Tarjeta:
# Constructor:
    def __init__(self, titular, cbu, banco, saldo, cod_ver):
        self.__titular = titular
        self.__cbu = cbu
        self.__banco = banco
        self.__saldo = saldo
        self.__cod_ver = cod_ver
# Mostrar con print:
    def __str__(self):
        cadena = str(f"Titular: {self.__titular} \n CBU: {self.__cbu} \n Banco: {self.__banco} \n Saldo: {self.__saldo} \n Código de verificación: {self.__cod_ver}")
        return cadena
# Getters:
    def get_titular(self):
        titular = self.__titular
        return titular
    def get_cbu(self):
        cbu = self.__cbu
        return cbu
    def get_banco(self):
        banco = self.__banco
        return banco
    def get_saldo(self):
        saldo = self.__saldo
        return saldo
    def get_cod_ver(self):
        cod_ver = self.__cod_ver
        return cod_ver
# Setters:
    def set_titular(self, titular):
        self.__titular = titular
    def set_cbu(self, cbu):
        self.__cbu = cbu
    def set_banco(self, banco):
        self.__banco = banco
    def set_saldo(self, saldo):
        self.__saldo = saldo
    def set_cod_ver(self, cod_ver):
        self.__cod_ver = cod_ver