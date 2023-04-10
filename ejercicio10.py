cantidad = int(input("Ingrese la cantidad de empleados: "))
empleado = []
sueldos = []
suma = []

for x in range(cantidad):
    nombre = input("Ingrese el nombre del empleado: ")
    empleado.append(nombre)
    sueldo1 = int(input("Ingrese el sueldo del primer mes: "))
    sueldo2 = int(input("Ingrese el sueldo del segundo mes: "))
    sueldo3 = int(input("Ingrese el sueldo del tercer mes: "))
    sueldos.append([sueldo1, sueldo2, sueldo3])

print("Empleado y sueldo de los ultimos 3 meses: ")
for x in range (cantidad):
    print(empleado[x], sueldos[x][0], sueldos [x][1], sueldos [x][2])

print("Es decir, cada empleado gano en los ultimos 3 meses:")
for x in range (cantidad):
    print(empleado[x], sueldos[x][0] + sueldos [x][1] + sueldos [x][2])
 
max_value = max(sueldos)
print("El maximo valor es la suma de estos tres sueldos: " , max_value)
