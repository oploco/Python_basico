def suma(*args):
    result=0
    i=0
    for arg in args:
        print('tipo param ', i, type(arg))
        if i==0:
            result= arg
        else:
            result +=arg
        i+=1
    print(result)


def resta(*args):
    result = 0
    i = 0
    for arg in args:
        print('tipo param ', i, type(arg))
        if i == 0:
            result = arg
        else:
            result -= arg
        i += 1
    print(result)


def multiplica(*args):
    result = 0
    i = 0
    for arg in args:
        print('tipo param ', i, type(arg))
        if i == 0:
            result = arg
        else:
            result *= arg
        i += 1
    print(result)

def division(*args):
    result = 0
    try:
        i = 0
        for arg in args:
            print('tipo param ', i, type(arg))
            if i == 0:
                result = arg
            else:
                result /= arg
            i += 1
        print(__name__,result)
    except ZeroDivisionError:
        print('error. Division por 0')
    except:
        print('error')

def salir():
    print('Saliendo')

def menu_principal():
    opciones = {
        '1': ('Sumar', suma),
        '2': ('Restar', resta),
        '3': ('Multiplicar', multiplica),
        '4': ('Dividir', division),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

if __name__ == '__main__':
    menu_principal()





