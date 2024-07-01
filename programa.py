from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto
import time

def crear_tienda():
    tipo = input("Ingrese el tipo de tienda\n [R]  Restaurante  \n [S]  Supermercado\n [F]  Farmacia\n ").upper().strip()
    if tipo == "R":
        nombre = input("Ingrese el nombre de la tienda: ")
        costo_delivery = float(input("Ingrese el costo de delivery: "))
        return Restaurante(nombre, costo_delivery)
    elif tipo == "S":
        nombre = input("Ingrese el nombre de la tienda: ")
        costo_delivery = float(input("Ingrese el costo de delivery: "))
        return Supermercado(nombre, costo_delivery)
    elif tipo == "F":
        print("INGRESE")
        nombre = input("Nombre de la tienda: ")
        costo_delivery = float(input("Costo de delivery: "))
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return None
    
def ingresar_productos(tienda):
    while True:
        print("Datos del producto:")
        nombre = input("Nombre    : ").lower()
        precio = float(input("Precio    : "))
        stock = int(input("Stock     : ") or 0)
        producto = Producto(nombre, precio, stock)
        tienda.ingresar_producto(producto)
        continuar = input("¿Desea ingresar otro producto? (s/n): ")
        if continuar.lower() != 's':
            break

def listar_productos(tienda):
    print("::::::::LISTADO DE PRODUCTOS:::::::")
    print(f"{tienda.listar_productos()}\n")
    time.sleep(2)

def realizar_venta(tienda):
    nombre_producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    tienda.realizar_venta(nombre_producto, cantidad)

def main():
    tienda = crear_tienda()
    if tienda:
        ingresar_productos(tienda)
        while True:
            accion = input("Seleccione una acción: \n1. Listar productos \n2. Realizar venta \n3. Salir \n")
            if accion == '1':
                listar_productos(tienda)
            elif accion == '2':
                realizar_venta(tienda)
            elif accion == '3':
                break
            else:
                print("Acción no válida.")

if __name__ == "__main__":
    main()