import ficheros

dic1={
        '1': 'Sumar',
        '2': 'Restar',
        '3': 'Multiplicar',
        '4': 'Dividir'
    }

dic2={
        '5': 'Salir',
        '7': 'Reiniciar'
    }

# para unir los diccionarios se usa |
dicR = dic1 | dic2
print(dicR)
print(dicR.values())
print(*dicR)

#probar escibir fichero
ficheros.escribir(dicR)