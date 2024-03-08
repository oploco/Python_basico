class calculadora():
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



calc=calculadora
print(calc.suma.__name__,calc.suma(2,2,3))
calc.resta(5,1)
calc.multiplica(3,7)
calc.division(6,2)




