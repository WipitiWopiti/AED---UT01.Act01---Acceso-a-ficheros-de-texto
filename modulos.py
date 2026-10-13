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
5. Archivar Módulo
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
                archivar_modulo()
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

    for directorio, subdirectorios, archivos in os.walk('./cuadernoDAM'):
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
    ruta = input("Introduce la ruta para el nuevo modulo, todo lo que no exista en esta ruta será creado: ")
    ruta = raiz / ruta
    ruta.mkdir(parents=True, exist_ok=True) # Parents=True permite crear todos los padres de la ruta de una
                                            # exist_ok=True Ignora el error por directorio existente en la ruta
    print(f"Modulo creado, la ruta completa es: {ruta}")
    return

def renombrar_modulo():
    '''Renombra el directorio de un modulo'''

    raiz = Path('./cuadernoDAM')
    ruta = input("Introduce la ruta del modulo que desee renombrar: ")
    ruta = raiz / ruta

    if ruta.exists():

        nuevo_nombre = input("Introduce el nuevo nombre a asignar: ")
        # with_name() mantiene toda la ruta y solo cambia el nombre del ultimo directorio
        nueva_ruta = ruta.with_name(nuevo_nombre)
        ruta.rename(nueva_ruta)
        print(f"Modulo renombrado a: {nueva_ruta}")
        return

    else:
        print("Error: La ruta introducida no existe.")
        return

def archivar_modulo():
    '''Mueve un modulo al archivo de primero'''
    
    raiz = Path('./cuadernoDAM')
    ruta = input("Introduzca la ruta al modulo que desea archivar: ")
    ruta_origen = raiz / ruta
    ruta_destino = Path(f"./cuadernoDAM/_primero/{ruta}")
    
    if ruta_origen.exists():
        os.replace(ruta_origen, ruta_destino)
        print("Modulo archivado")
        return

    else:
        print("Error: La ruta introducida no existe.")
        return

def eliminar_modulo():
    '''Elimina un módulo'''
    
    print("ADVERTENCIA: Esta funcionalidad borra el módulo con todo su contenido")
    raiz = Path('./cuadernoDAM')
    ruta = input("Introduzca la ruta al módulo que desea borrar: ")
    ruta = raiz / ruta

    try:
        os.rmdir(ruta)
        print("Modulo eliminado")
        return
        
    except:
        print("Error, no se ha encontrado la ruta especificada")
        return
    

