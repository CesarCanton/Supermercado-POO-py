import csv
# from classes.usuario import Usuario

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
            if usuario["userName"] == userName:
                return usuario
        return None
    
    def agregaUsuario(self, usuario):
        with open(self.rutaArchivo, 'a', newline='', encoding='utf-8') as archivo:
            campos = ['id', 'nombres', 'apellidos', 'userName', 'contra', 'rol', 'primerIngreso']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writerow({
                'id': usuario.id,
                'nombres': usuario.nombres,
                'apellidos': usuario.apellidos,
                'userName': usuario.userName,
                'contra': usuario.contra,
                'rol': usuario.rol,
                'primerIngreso': usuario.primerIngreso
            })
            
    def actualizarContraseña(self, usuario):
        usuarios = self.obtenerUsuarios()
        with open(self.rutaArchivo, 'w', newline='', encoding='utf-8') as archivo:
            campos = ['id', 'nombres', 'apellidos', 'userName', 'contra', 'rol', 'primerIngreso']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for u in usuarios:
                if u["userName"] == usuario["userName"]:
                    escritor.writerow(usuario)
                else:
                    escritor.writerow(u)