import csv

class FacturaRepository:

    def __init__(self, rutaArchivo):
        self.rutaArchivo = rutaArchivo

    def obtenerFacturas(self):
        facturas = []
        with open(self.rutaArchivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                facturas.append(fila)
        return facturas
    
    