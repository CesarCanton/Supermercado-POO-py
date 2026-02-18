import os
import sys
from infrastructure.usuarioRepository import UsuarioRepository
from services.usuarioService import actualizarContraseña


titulo = "\n\033[1;36;40m SUPER MERCADO\033[0m\n"

def mostrarMenuCliente(usuario):
    os.system('cls')
    print(titulo)
    if usuario["primerIngreso"]:
        primerIngresoInterface(usuario)
    print(f"Bienvenido, {usuario["nombres"]} {usuario["apellidos"]}!\n")
    print("Que es lo que deseas hacer?\n")
    while True:
        try:
            opcion=int(input("\n1.Comprar\n2.Ver facturas pasadas\n3.Actualizar mis datos\n4.Cerrar sesion\n"))
            match opcion:
                case 1:comprar()
                case 2:verFacturas()
                case 3:actualizarDatos()
                case 4:
                    print("Cerrando sesion...")
                    sys.exit()
                    
                    
                    break
                case _:
                    print("Opcion fuera del rango, vuelva a intentarlo")
        
        
        except:
            pass
        
def primerIngresoInterface(usuario):
    os.system('cls')
    print(titulo)
    print("Bienvenido a Super Mercado, para continuar con tu experiencia, por favor ingresa una nueva contraseña\n")
    while True:
        nuevaContra = input("Nueva contraseña: ")
        confirmarContra = input("Confirmar contraseña: ")
        if nuevaContra == confirmarContra:
            usuario["contra"] = nuevaContra
            usuario["primerIngreso"]=False
            actualizarContraseña(usuario, nuevaContra)
            mostrarMenuCliente(usuario)
            break
        else:
            print("\nLas contraseñas no coinciden. Por favor, intenta de nuevo.\n")



def comprar():
    pass

def actualizarDatos():
    pass

def verFacturas():
    pass
