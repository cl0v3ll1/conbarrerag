
print ("¿Cuantos productos llevara?")
cantp=int(input())
total=0

for i in range(cantp):
    print ("¿Que vas a llevar? \n 1.- Jugo $1000 \n 2.- Pasta de dientes $2000 \n 3.- Pan de molde $3000 \n 4.- Salir")
    op=int(input())

    if op==1:
        print("Usted llevara jugo")
        total+=1000
    elif op==2:
        print("Usted llevara Pasta de dientes")
        total+=2000
    elif op==3:
        print("Usted llevara Pan de molde")
        total+=3000
    elif op==4:
        print("Elige otra opcion")

print(f"Su total sera de ${total}")
print(f"Mas el IVA {total*1.19:.0f}")