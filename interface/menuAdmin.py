# from infrastructure.usuarioRepository import UsuarioRepository
import os
from services.usuarioService import crearUsuario
from services.productoService import crearProducto
from services.productoService import obtenerProductos
from infrastructure.productoRepository import productoRepository

titulo = "\n\033[1;36;40m SUPER MERCADO (admin)\033[0m\n"

def mostrarMenuAdmin(usuario):
    os.system('cls')
    print(titulo)
    
    print("ELIGE UNA OPCION DE ADMINISTRADOR\n")
    
    while True:
        try:
            opcion=int(input("1.Creacion de usuarios\n2.Gestion de productos\n3.Informe de productos\n"))
            match opcion:
                case 1:
                    print("Creacion de usuarios")
                    crearUsuarioInterface(usuario)
                case 2:
                    print("Gestion de productos")
                    gestionProductosInterface(usuario)
                case 3:
                    print("Informde productos")
                    informeProductosInterface(usuario)
                case _:
                    print("Opcion fuera del rango, vuelva a intentarlo")
                    
        except ValueError:
            print("Error a la hora de ingresar el valor, vuelva a intentarlo: "+str(ValueError))
                    

def crearUsuarioInterface(usuario):
    os.system('cls')
    print(titulo)
    print("Creando Usuario, ingrese adecuadamente los datos\n")
    nombres=input("\nNombres:").strip()
    apellidos=input("\napellidos:").strip()
    contra=input("\nContraseña: ").strip()
    try:
        crearUsuario(nombres, apellidos, contra)
        
    except Exception as e:
        print(f"Ocurrió un problema al crear el usuario: {e}")
    
    mostrarMenuAdmin(usuario)
    
    
    
def gestionProductosInterface(usuario):
    os.system('cls')
    print(titulo)
    print("Gestion de productos\n")
    
    opcion=int(input("\n1.Crear producto\n2.Eliminar producto\n3.Volver al menu principal\n"))
    
    while True:
        match opcion:
            case 1:
                crearProductoInterface(usuario)
                break
            case 2:
                eliminarProductoInterface(usuario)
                break
            case 3:
                mostrarMenuAdmin(usuario)
                break
            case _:
                print("Opcion fuera del rango, vuelva a intentarlo")
                break
            
    
    


def crearProductoInterface(usuario):
    os.system('cls')
    print(titulo)
    
    while True:
        print("Creacion de producto")
        print("Ingrese adecuadamente los datos")
        
        # Validar nombre
        while True:
            nombre = input("\nNombre del producto: ").strip()
            if nombre == "":
                print("El nombre del producto no puede estar vacío")
            else:
                break
        
        while True:
            precioInput = input("\nPrecio del producto: ").strip()
            try:
                precio = float(precioInput)
                if precio <= 0:
                    print("El precio del producto debe ser mayor a 0")
                else:
                    break
            except ValueError:
                print("Debe ingresar un número válido para el precio")
        
        while True:
            stockInput = input("\nStock del producto: ").strip()
            try:
                stock = int(stockInput)
                if stock < 0:
                    print("El stock del producto no puede ser negativo")
                else:
                    break
            except ValueError:
                print("Debe ingresar un número entero válido para el stock")
        
        categoriasValidas = [1, 2, 3, 4, 5]
        while True:
            categoriaInput = input("\nCategoria del producto (1: Bebidas, 2: Lacteos, 3: Abarrotes, 4: Limpieza, 5: Snacks): ").strip()
            try:
                categoriaId = int(categoriaInput)
                if categoriaId not in categoriasValidas:
                    print("La categoría debe ser 1, 2, 3, 4 o 5")
                else:
                    break
            except ValueError:
                print("Debe ingresar un número entero válido para la categoría")
        
        try:
            crearProducto(nombre, precio, stock, categoriaId)
            print("Producto creado exitosamente.")
            break
        except Exception as e:
            print(f"Ocurrió un problema al crear el producto: {e}")

def eliminarProductoInterface(usuario):
    os.system('cls')
    print(titulo)
    print("Eliminar producto")
    print ("Lista de productos disponibles:\n")
    productos = obtenerProductos()
    for producto in productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")
    idProducto = input("\nIngrese el ID del producto que desea eliminar: ").strip()
    repo = productoRepository("data/productos.txt")
    producto = repo.obtenerProductoPorId(idProducto)
    if producto:
        repo.eliminarProducto(idProducto)
        print("Producto eliminado exitosamente.")
    else:
        print("No se encontró un producto con el ID proporcionado.")
    mostrarMenuAdmin(usuario)
    
def informeProductosInterface(usuario):
    os.system('cls')
    print(titulo)
    print("Informe de productos\n")
    productos = obtenerProductos()
    for producto in productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")
    input("\nPresione Enter para volver al menú principal...")
    mostrarMenuAdmin(usuario)
    
    