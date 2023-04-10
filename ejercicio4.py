ip=[]

cant=int(input("Ingrese la cantidad de IP: "))

for x in range(cant):
    numero=input("Ingrese el IP: ")
    ip.append(numero)

print("Las IP ingresadas son: ")
print(ip)