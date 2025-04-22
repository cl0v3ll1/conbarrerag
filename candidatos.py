c1="John Pork"
c2="Quandale Dingle"
cantvotos1=0
cantvotos2=0

cantV=int(input("Ingrese la cantidad de votantes :"))
for i in range(cantV):
    print(f"¿Por quien votara?:\n 1.-{c1}, 2.-{c2}")
    voto=int(input())

    if voto==1:
        print(f"Eligiste a {c1}")
        cantvotos1=cantvotos1+1 
    elif voto==2:
        print(f"Eligiste a {c2}")
        cantvotos2=cantvotos2+1
    else:
        print("Nulo")
      

if cantvotos1>cantvotos2:
    print("Gano John Pork")
elif cantvotos1==cantvotos2:
    print("Empate")
else:
    print("Gano Quandale Dingle")
