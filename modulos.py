from pathlib import Path
import os

def menu_modulos():
    '''Bucle del menú para las operaciones CRUD de los directorios'''

    while True:
        print(f'''
===== MENÚ MÓDULOS =====
1. Comprobar si módulo existe
2. Listar módulos
3. Crear Módulo
4. Renombrar modulo
5. Mover Módulo
6. Eliminar Módulo
9. Salir''')

        try:
            inp = int(input("Seleccione una opción: "))
        except:
            print("Debe introducir un numero")
            continue

        match inp:
            case 1:
                modulo_existe()
            case 2:
                listar_modulos()
            case 3:
                crear_modulo()
            case 4:
                renombrar_modulo()
            case 5:
                mover_modulo()
            case 6:
                eliminar_modulo()
            case 9:
                print("Regresando al menú principal")
                return
            case _:
                print("Debe introducir un numero dentro de las opciones.")
                continue

def modulo_existe():
    '''Comprueba si el modulo existe'''

    modulo_buscar = input("Introduzca el nombre del modulo que desea buscar: ")

    for directorio, subdirectorios, archivos in os.walk('.\cuadernoDAM'):
        for subdirectorio in subdirectorios:
            if modulo_buscar == subdirectorio:
                print(f"Modulo encontrado en {directorio}")
                return
        
    print("Modulo no encontrado")
    return
            
    
def listar_modulos():
    '''Lista los modulos del cuaderno de un modulo'''

    # Sale un poco feo pero yo no soy diseñador lo siento
    for directorio, subdirectorios, archivos in os.walk('./cuadernoDAM'):
        print(f"Directorio: {directorio}")
        for subdirectorio in subdirectorios:
            print(f" --- {subdirectorio}")
    
    return

def crear_modulo():
    '''Crea un modulo donde decida el usuario'''

    raiz = Path('./cuadernoDAM')
    ruta_inp = input("Introduce la ruta donde quieras crear el modulo: ")
    nuevo_modulo = input("Introduce el nombre del nuevo módulo: ")
    ruta = raiz / ruta_inp / nuevo_modulo
    print(ruta)
    ruta.mkdir(parents=True, exist_ok=True)

def renombrar_modulo():
    '''Renombra el directorio de un modulo'''

def mover_modulo():
    '''Mueve un modulo al archivo de primero'''

def eliminar_modulo():
    '''Elimina un módulo'''

