class Estudiante():
    num_cuantos=0

    def __init__(self,vnom,vape):
        self.nombre = vnom
        self.apellido = vape

estudiantes = []
cuantos=input('Nº alumnos:')

Estudiante.num_cuantos = cuantos

for i in range(int(Estudiante.num_cuantos)):
    print('-----------Alumno---------- ',i+1)
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')

    estudiante = Estudiante(nombre,apellido)

    estudiantes.append(estudiante)

print(estudiantes)

i=1
for al in estudiantes:
    print(f'Alumno {i} {al.nombre} {al.apellido}' )
    i+=1