from services import usuarioService



class Usuario:
    def __init__(self, id, nombres, apellidos, userName, contra, rol, primerIngreso):
        self.id=id
        self.nombres=nombres
        self.apellidos=apellidos
        self.userName=userName
        self.contra=contra
        self.rol=rol
        self.primerIngreso=primerIngreso
        
    