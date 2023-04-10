productos = []
precios = []
cant = int(input("Ingrese la cantidad de productos que agregara al sistema: "))

for x in range(cant):
    producto = input("Ingrese producto:")
    productos.append(producto)
    precio =int(input("Ingrese el precio del producto:"))
    precios.append(precio)

cantidad = 0
for x in range(cant):
    if precios[x] > precios[0]:
        cantidad = cantidad+1

print("Cantidad de productos con un precio mayor al primer producto: ")
print(cantidad)