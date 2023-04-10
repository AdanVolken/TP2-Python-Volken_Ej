# lista = []
# sueldos = int(input("Ingrese la cantidad de sueldos que se agregaran: "))
# x = 0
# for x in range(sueldos):
#     sueldo= int(input("Ingrese un sueldo: "))
#     lista.append(sueldo)
#     x=x+1

# for k in range(sueldos):
#     for x in range(sueldos):
#         if lista[x]>lista[x+1]:
#             aux=lista[x]
#             lista[x]=lista[x+1]
#             lista[x+1]=aux

# print("Lista ordenada")
# print(lista)


sueldos=[]
cantidad = int(input("Ingrese la cantidad de sueldos que se agregaran: "))
for x in range(cantidad):
    valor=int(input("Ingrese sueldo:"))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for k in range(cantidad-1):
    for x in range(cantidad-1):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print("Lista ordenada")
print(sueldos)

