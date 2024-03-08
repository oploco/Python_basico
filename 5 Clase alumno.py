# Definir una clase estudiante, crear varios estudiantes y meterlos en una lista
class Estudiante():

    def __init__(self,vnom,vape):
        self.nombre = vnom
        self.apellido = vape


estudiantes = []
cuantos=input('Nº alumnos:')

for i in range(int(cuantos)):
    print('-----------Alumno---------- ',i+1)
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')

    estudiante = Estudiante(nombre,apellido)

    estudiantes.append(estudiante)


print(estudiantes)

i=1
for al in estudiantes:
    i+=1
    print(f'Alumno {i} {al.nombre} {al.apellido}' )

