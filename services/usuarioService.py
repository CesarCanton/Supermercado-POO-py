
from infrastructure.usuarioRepository import UsuarioRepository
from classes.usuario import Usuario

def crearUsuario(nombres, apellidos, contra):
    # Valores por defecto
    primerIngreso=True
    rol="CLIENTE"
    
    repo = UsuarioRepository("data/usuarios.txt")
    usuarios = repo.obtenerUsuarios()
    id = len(usuarios) + 1
    userName = crearUsername(nombres, apellidos, id)
    nuevoUsuario = Usuario(id, nombres, apellidos, userName, contra, rol, primerIngreso)
    repo.agregaUsuario(nuevoUsuario)
    


def crearUsername(nombres, apellidos, id):
    userName=nombres[0].upper()+apellidos[0].upper()+str(id)
    return userName

def actualizarContraseña(usuario, nuevaContra):
    repo = UsuarioRepository("data/usuarios.txt")
    usuario["contra"] = nuevaContra
    usuario["primerIngreso"]=False
    repo.actualizarContraseña(usuario)