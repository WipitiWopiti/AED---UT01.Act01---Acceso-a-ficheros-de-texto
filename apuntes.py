def menu_apuntes():
    '''Bucle del menú para las operaciones CRUD de los ficheros'''
    
    while True:
        print(f'''
===== MENÚ APUNTES =====
1. Comprobar si apuntes existen
2. Listar apuntes
3. Crear apuntes
4. Leer y modificar el contenido de unos apuntes
5. Renombrar apuntes
6. Mover apuntes
7. Eliminar apuntes
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
                modificar_fichero()
            case 5:
                renombrar_fichero()
            case 6:
                mover_fichero()
            case 7:
                eliminar_fichero()
            case 9:
                print("Regresando al menú principal")
                return
            case _:
                print("Debe introducir un numero dentro de las opciones.")
                continue

def fichero_existe():
    '''Comprueba si el modulo existe'''

def listar_ficheros():
    '''Lista los apuntes de un modulo'''

def crear_fichero():
    '''Crea un modulo donde decida el usuario'''

def mover_fichero():
    '''Mueve un modulo al archivo de primero'''

def eliminar_fichero():
    '''Elimina un módulo'''

