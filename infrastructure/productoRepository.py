import csv

class productoRepository:

    def __init__(self, rutaArchivo):
        self.rutaArchivo =rutaArchivo

    def obtenerProductos(self):
        productos = []
        with open(self.rutaArchivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                productos.append(fila)
        return productos
    
    def agregarProducto(self, producto):
        with open(self.rutaArchivo, 'a', newline='', encoding='utf-8') as archivo:
            campos = ['id', 'nombre', 'precio', 'stock','categoriaId','activo']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writerow({
                'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'stock': producto.stock,
                'categoriaId': producto.categoriaId,
                'activo': producto.activo
            })
    
    def obtenerProductoPorId(self, id):
        productos = self.obtenerProductos()
        for producto in productos:
            if producto["id"] == id:
                return producto
        return None
    
    def eliminarProducto(self, id):
        productos = self.obtenerProductos()
        productosActualizados = [producto for producto in productos if producto["id"] != id]
        with open(self.rutaArchivo, 'w', newline='', encoding='utf-8') as archivo:
            campos = ['id', 'nombre', 'precio', 'stock','categoriaId','activo']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for producto in productosActualizados:
                escritor.writerow(producto)