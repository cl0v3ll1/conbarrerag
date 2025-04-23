print("Ingresa la cantidad de notas")
suma=0
notasazules=0
cantn=int(input())
for i in range (cantn):
    print ("ingrese la nota ",i +1)
    nota=float(input())
    suma=suma+nota
    if nota>=4:
        notasazules+=1

prom=suma/cantn
print("Su promedio es ", prom)
print(f"Obtuvo {notasazules} notas sobre 4")

if prom>=4:
    print("El alumno aprobo")
else:
    print("El alumno reprobo")
