from services import usuarioService



class Usuario:
    def __init__(self, id, nombres,apellidos,contraseña,rol, primerIngreso=True):
        self.id=id
        self.nombres=nombres
        self.apellidos=apellidos
        self.contraseña=contraseña
        self.rol=rol
        self.primerIngreso=primerIngreso
        
    