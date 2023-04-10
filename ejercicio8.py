alumno = []
nota = []
cant = int(input("Ingrese la cantidad de alumnos: "))

for x in range(cant):
    nombre = input("Ingrese el nombre del alumno: ")
    alumno.append(nombre)
    cali= int(input("Ingrese la calificacion del alumno: "))
    nota.append(cali)


rango=0
for x in range(cant):
    print(alumno[x])
    print(nota[x])
    if nota[x] >= 8:
        print("Muy bueno")
        rango= rango+1
    else:
        if nota[x] >= 4:
            print("Bueno")
        else:
            print("Insuficiente")

print("Cantidad de alumnos con muy bueno: " , rango)