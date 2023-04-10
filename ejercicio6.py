pais = []
poblacion = []

cantidad= int(input("Ingrese la cantidad de paises: "))

for x in range(cantidad):
    paises= input("Ingrese un pais: ")
    habitantes= int(input("Ingrese cantidad de habitantes por pais: "))
    pais.append(paises)
    poblacion.append(habitantes)


print("Lista de paises desordenada" , pais)

for k in range(cantidad - 1):
    for x in range(cantidad-1):
        if poblacion[x]<poblacion[x+1]:
            aux=poblacion[x]
            poblacion[x]=poblacion[x+1]
            poblacion[x+1]=aux
print("Lista ordenada" , poblacion)
