lista = []
cantidad = int(input("Ingrese la cantidad de ciudades: "))

x = 0
for x in range (cantidad):
    ciudad = input("Ingresee ciudad: ")
    lista.append(ciudad)

city= input("Repite ciudad ingresada: ")
if city in lista:
    print(lista.index(city))
else:
    print("La ciudad no esta")
