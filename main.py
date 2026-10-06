import modulos as modulos
import apuntes as apuntes

def main():
    '''Bucle menú principal'''
    
    while True:
        print(f'''===== GESTOR DE APUNTES Y MÓDULOS ===== \n''')
        print("Presione 9 para salir")

        try:
            inp = int(input("Desea trabajar con módulos (1) o apuntes (2)?: "))
        except:
            print("Debe introducir un numero")
            continue

        match inp:
            case 1:
                modulos.menu_modulos()
            case 2:
                apuntes.menu_apuntes()
            case 9:
                exit()
            case _:
                print("Debe introducir un numero dentro de las opciones.")
                continue

if __name__ == "__main__":
    main()