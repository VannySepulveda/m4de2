from producto import Producto
from abc import ABC, abstractmethod

class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self.nombre = nombre
        self.costo_delivery = costo_delivery
        self.productos = []

    def ingresar_producto(self, producto):
        for p in self.productos:
            if p == producto:
                p + producto
                return
        self.productos.append(producto)

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass

class Restaurante(Tienda):
    def ingresar_producto(self, producto):
        producto.stock = 0
        super().ingresar_producto(producto)

    def listar_productos(self):
        return "\n".join([f"{p.nombre} - ${p.precio}" for p in self.productos])

    def realizar_venta(self, nombre_producto, cantidad):
        pass

class Supermercado(Tienda):
    def listar_productos(self):
        productos_listados = []
        
        for p in self.productos:
            stock_message = f"Pocos productos disponibles - Stock: {p.stock}" if p.stock < 10 else f"Stock: {p.stock}"
            productos_listados.append(f"{p.nombre} - ${p.precio} - {stock_message}")
        return "\n".join(productos_listados)
        

    def realizar_venta(self, nombre_producto, cantidad):
        for p in self.productos:
            if p.nombre == nombre_producto:
                if p.stock >= cantidad:
                    p - cantidad
                else:
                    p.stock = 0
                return

class Farmacia(Tienda):
    def listar_productos(self):
        productos_listados = []
        for p in self.productos:
            precio_message = f"${p.precio}"
            if p.precio > 15000:
                precio_message += " - Envío gratis al solicitar este producto"
            productos_listados.append(f"{p.nombre} - {precio_message}")
        return "\n".join(productos_listados)

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            return
        for p in self.productos:
            if p.nombre == nombre_producto:
                if p.stock >= cantidad:
                    p - cantidad
                else:
                    p.stock = 0
                return