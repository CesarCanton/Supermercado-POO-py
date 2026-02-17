class AuthService:

    def __init__(self, usuarioRepository):
        self.usuarioRepository = usuarioRepository

    def login(self, userName, contra):

        if not userName.strip() or not contra.strip():
            return None, "Campos vacíos no permitidos"

        usuario = self.usuarioRepository.buscarPorUsername(userName)

        if usuario is None:
            return None, "Usuario no existe"

        if usuario["contra"] != contra:
            return None, "Contraseña incorrecta"

        return usuario, None
