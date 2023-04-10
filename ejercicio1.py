lista = []
for x in range(5):
    valor = int(input("Ingrese el valor: (si engresa 0 la lista termina!) "))
    lista.append(valor)
    if valor==0:
        print("Si ingresa el numero 0, la lista termina")
        break

print("Lista completa")
print(len(lista))


lista=[]
valor=int(input("Ingresar valor (0 para finalizar):"))
while valor!=0:
    lista.append(valor)
    valor=int(input("Ingresar valor (0 para finalizar):"))

print("Tamano de la lista:")
print(len(lista))


