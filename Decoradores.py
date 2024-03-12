def decorador(func):
    def inner1(*args,**kwards):
        print('inicio')
        return none

    return inner1()


@decorador
def hola():
    print('hola')


print(hola())
