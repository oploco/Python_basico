f = open('primer fichero.txt', 'a')
#with open('primer fichero.txt', 'a') as f:

try:
    def escribir(values):
        ''' Escribe en fichero '''
        f = open('primer fichero.txt', 'a')
        #with open('primer fichero.txt', 'a') as f:

        #if type(value) == 'dict':  no furula
        if isinstance(values, dict):
            for key, value in values.items():
                #f.write(str(*value) + '\n')
                f.write(key + ':' + value + '\n')
                print('guardado dict',key + ':' + value)
        else:
            f.write(values + '\n')
            print('guardado', values)


    def inicio():
        f = open('primer fichero.txt', 'a')
        for i in range(10):
            f.writelines('linea número ' + str(i) + '\n')
finally:
    f.close()