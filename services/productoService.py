from infrastructure.productoRepository import productoRepository
from classes.producto import Producto

def crearProducto(nombre, precio, stock, categoriaId):
    repo = productoRepository("data/productos.txt")
    productos = repo.obtenerProductos()
    id = len(productos) + 1
    activo = True
    nuevoProducto = Producto(id, nombre, precio, stock, categoriaId, activo)
    repo.agregarProducto(nuevoProducto)
    
def obtenerProductos():
    repo = productoRepository("data/productos.txt")
    return repo.obtenerProductos()