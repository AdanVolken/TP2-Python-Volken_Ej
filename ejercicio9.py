palabras=[]
can=int(input("Ingrese la cantidad de palabras: "))

for x in range(can):
    pal=str(input("Ingresa la Palabra: "))
    if len(pal)>5:
        pal=pal[:5]+"@"
    cambio=pal.replace(" ","")
    palabras.append(cambio)



print (palabras)