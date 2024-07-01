class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, precio):
        self.__precio = precio
        
    @stock.setter
    def stock(self, cantidad):
        self.__stock = max(0, cantidad)

    def __eq__(self, otro):
        return self.__nombre == otro.__nombre

    def __add__(self, otro):
        if self == otro:
            self.stock += otro.stock
            self.precio = otro.precio
        return self


    def __sub__(self, cantidad):
        self.stock -= cantidad
        return self

    def __str__(self):
        return f"{self.__nombre} -     ${self.__precio} -     Stock: {self.__stock}"