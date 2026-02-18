import os
from infrastructure.usuarioRepository import UsuarioRepository
from services.authService import AuthService
from interface.menuAdmin import mostrarMenuAdmin
from interface.menuCliente import mostrarMenuCliente


titulo = "\n\033[1;36;40m SUPER MERCADO \033[0m\n"
repo = UsuarioRepository("data/usuarios.txt")
authSer = AuthService(repo)

def mostrarMenuPrincipal():
    os.system('cls')
   
    
    print(titulo)
    print("\n\nElija una opcion\n\n")
    
    while True:
        try:
            opcion = int(input("1.Iniciar Sesion\n2.Salir\n"))
            if opcion == 1:
                iniciarSesion()
            elif opcion == 2:
                print("Saliendo del sistema")
                break
            else:
                print("Opcion fuera del rango, vuelva a intentarlo")
        except ValueError:
            print("Error a la hora de ingresar el valor, vuelva a intentarlo")

def iniciarSesion():
    os.system('cls')
    print(titulo)
    print("\nINICIAR SESION\n")
    
    while True:
        try:
            usuario = input("\nUsuario:").strip()
            contra = input("\nContraseña:").strip()
            usuarioObj, error = authSer.login(usuario, contra)
            
            if error or usuarioObj is None:
                print("\nError de inicio de sesion")
                continue
            
            match usuarioObj["rol"]:
                case "ADMIN":
                    mostrarMenuAdmin(usuarioObj)
                    break
                    
                case "CLIENTE":
                    mostrarMenuCliente(usuarioObj)
                    break
                case _:
                    print("Rol Indefinido")
                
                
        except Exception as e:
            print(f"Ocurrió un problema: {e}")