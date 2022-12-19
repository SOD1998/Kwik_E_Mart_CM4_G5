# Clase: Domicilio
class Domicilio:
# Constructor:
    def __init__(self, provincia, ciudad, cp, calle_1, calle_2, num_casa, num_piso):
        self.__calle_1 = calle_1
        self.__calle_2 = calle_2
        self.__num_casa = num_casa
        self.__num_piso = num_piso
        self.__ciudad = ciudad
        self.__provincia = provincia
        self.__cp = cp
# Mostrar con print
    def __str__(self):
        cadena = str(f"Provincia: {self.__provincia} \n Ciudad: {self.__ciudad} \n Código Postal: {self.__cp} \n Calles: {self.__calle_1} y {self.__calle_2} \n Casa: {self.__num_casa} \n Piso: {self.__num_piso}")
        return cadena
# Getters:
    def get_provincia(self):
        provincia = self.__provincia
        return provincia
    def get_ciudad(self):
        ciudad = self.__ciudad
        return ciudad
    def get_cp(self):
        cp = self.__cp
        return cp
    def get_calle_1(self):
        calle_1 = self.__calle_1
        return calle_1
    def get_calle_2(self):
        calle_2 = self.__calle_2
        return calle_2
    def get_num_casa(self):
        num_casa = self.__num_casa
        return num_casa
    def get_num_piso(self):
        num_piso = self.__num_piso
        return num_piso
# Setters:
    def set_provincia(self, provincia):
        self.__provincia = provincia
    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad
    def set_cp(self, cp):
        self.__cp = cp
    def set_calle_1(self, calle_1):
        self.__calle_1 = calle_1
    def set_calle_2(self, calle_2):
        self.__calle_2 = calle_2
    def set_num_casa(self, num_casa):
        self.__num_casa = num_casa
    def set_num_piso(self, num_piso):
        self.__num_piso = num_piso