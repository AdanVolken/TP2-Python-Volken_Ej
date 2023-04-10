cantidad = int(input("Ingrese la cantidad de paises: "))
paises = []
temperaturas = []
promedio = []

for x in range(cantidad):
    nombre = input("Ingrese el nombre del pais: ")
    paises.append(nombre)
    temp1 = int(input("Ingrese primer temperatura: "))
    temp2 = int(input("Ingrese segundo temperatura: "))
    temp3 = int(input("Ingrese tercer temperatura: "))
    temperaturas.append([temp1, temp2, temp3])

print("Pais y temperatura media de los ultimos 3 meses: ")
for x in range(cantidad):
    print(paises[x], temperaturas[x][0], temperaturas[x][1], temperaturas[x][2])

for x in range(cantidad):
    pro= (temperaturas[x][0] + temperaturas[x][1] + temperaturas[x][2]) /3
    promedio.append(pro)

print("Listado de paises y el promedio de las temperaturas trimestrales: ")
for x in range(cantidad):
    print(paises[x], promedio[x])

mayor = 0
for x in range(cantidad):
    if promedio[x] > promedio[mayor]:
        mayor=x

print("Pais con temperatura media trimestral mayor: " ,paises[mayor])
