from pathlib import Path
import os

def menu_apuntes():
    '''Bucle del menú para las operaciones CRUD de los ficheros'''
    
    while True:
        print(f'''
===== MENÚ APUNTES =====
1. Comprobar si apuntes existen
2. Listar apuntes
3. Crear apuntes
4. Leer y modificar el contenido de unos apuntes
5. Mostrar nombre, asignatura y ruta de un fichero
6. Renombrar apuntes
7. Mover apuntes
8. Eliminar apuntes
9. Salir''')

        try:
            inp = int(input("Seleccione una opción: "))
        except:
            print("Debe introducir un numero")
            continue

        match inp:
            case 1:
                fichero_existe()
            case 2:
                listar_ficheros()
            case 3:
                crear_fichero()
            case 4:
                leer_y_modificar_fichero()
            case 5:
                info_fichero()
            case 6:
                renombrar_fichero()
            case 7:
                mover_fichero()
            case 8:
                eliminar_fichero()
            case 9:
                print("Regresando al menú principal")
                return
            case _:
                print("Debe introducir un numero dentro de las opciones.")
                continue

def fichero_existe():
    '''Comprueba si el modulo existe'''
    
    fichero_buscar = input("Introduzca el nombre del modulo que desea buscar: ")
    
    for directorio, subdirectorios, archivos in os.walk('./cuadernoDAM'):
        for archivo in archivos:
            if fichero_buscar == archivo:
                print(f"Fichero encontrado en {directorio}")
                return
            
    print("Modulo no encontrado")
    return

def listar_ficheros():
    '''Lista los apuntes de un modulo'''
    
    # REVISAR LUEGO
    ruta = input("Introduzca la ruta donde desee listar los apuntes: ")
    for archivo in os.walk(ruta):
        print(f"- {archivo}")
        

def crear_fichero():
    '''Crea un fichero donde decida el usuario'''
    
    ruta = input("Introduzca la ruta donde desee crear los apuntes: ")
    nombre_fichero = input("Introduzca el nombre que quiere que tenga el fichero, introduzcalo junto a la extension. Ejemplo: apunte.txt: ")
    ruta = Path(ruta) / nombre_fichero
    
    try:
        # Creamos el fichero, si la ruta está mal salta error
        ruta.touch()
        print(f"Fichero {nombre_fichero} creado correctamente")
        return
    except:
        print("Error, la ruta especificada no existe")
        return

def leer_y_modificar_fichero():
    '''Permite leer y modificar el contenido de un fichero'''
    
    fichero = input("Introduzca el nombre del fichero: ")
    for archivo in os.walk("./cuadernoDAM"):
        if fichero == archivo:
            print("Apuntes encontrados")
            inp = input("Desea (L)eer o (M)odificar los apuntes?: ").strip().upper()

            match inp:
                case "L":
                    with open(archivo, "r") as f:
                        contenido = f.read()
                        print(contenido)
                case "M":
                    contenido_volcar = input("Introduzca el contenido a añadir: ")
                    with open(archivo, "a") as f:
                        archivo.write(f"\n {contenido_volcar}")
                case _:
                    print("Error. Introduzca un valor válido.")
                    return
    return


def info_fichero():
    '''Muestra el titulo, la asignatura y la ruta del fichero'''

    fichero_buscar = input("Introduzca el nombre del fichero a buscar: ")
    for directorio, subdirectorios, archivos in os.walk('./cuadernoDAM'):
        if fichero_buscar == archivos:
            print(f'''ARCHIVO ENCONTRADO:
            NOMBRE: {archivos}
            ASIGNATURA: {subdirectorios}
            RUTA: {directorio}''')
            return

    print("Error. Apunte no encontrado")
    return
    
def renombrar_fichero():
    '''Cambia el nombre de un fichero'''

    fichero_buscar = input("Introduzca el nombre del fichero a buscar: ")
    for directorio, subdirectorios, archivos in os.walk('./cuadernoDAM'):
        if fichero_buscar == archivos:
            print("Fichero encontrado")
            nuevo_nombre = input("Introduzca el nuevo nombre para el fichero: ")
            os.rename(archivos, nuevo_nombre)
            print(f"Apunte renombrado correctamente a {nuevo_nombre}")
            return

    print("Error. Apuntes no encontrados")
    return

def mover_fichero():
    '''Mueve un modulo al archivo de primero'''

    ruta = input("Introduzca la ruta al fichero que desea archivar: ")
    ruta = Path(ruta)
    ruta_archivo = Path("./cuadernoDAM/_primero")
    
    if ruta.exists():
        os.rename(ruta, ruta_archivo)       # os.rename permite además de cambiar el nombre, cambiar la ruta de un archivo o directorio
        print("Modulo archivado")
        return

    else:
        print("Error: La ruta introducida no existe.")
        return

def eliminar_fichero():
    '''Elimina un módulo'''

    ruta = input("Introduzca la ruta al fichero que desea borrar: ")
    try:
        os.rmdir(ruta)
        print("Apunte eliminado")
        return
        
    except:
        print("Error, no se ha encontrado la ruta especificada")
        return
