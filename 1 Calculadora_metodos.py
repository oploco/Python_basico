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
    print('Resultado: ' , result)


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
    print('Resultado: ' , result)


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
    print('Resultado: ' , result)

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


print(suma.__name__,suma(2.3,2.5,3))
resta(5.3,1)
multiplica(3,7)
division(6,2)




