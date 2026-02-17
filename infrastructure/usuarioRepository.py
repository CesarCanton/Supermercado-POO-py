import csv

class UsuarioRepository:

    def __init__(self, rutaArchivo):
        self.rutaArchivo =rutaArchivo

    def obtenerUsuarios(self):
        usuarios = []
        with open(self.rutaArchivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                usuarios.append(fila)
        return usuarios

    def buscarPorUsername(self, userName):
        usuarios = self.obtenerUsuarios()
        for usuario in usuarios:
            if usuario["username"] == userName:
                return usuario
        return None
    
    