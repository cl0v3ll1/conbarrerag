import time

CantDetergente=2

print("Es un dia normal, estas sentado y flojeando y de la nada te acuerdas que no lavaste la ropa en toda la semana. Te paras y te dirijes al baño, abres la lavadora")
time.sleep(1)
print(f"Vas a lavar tu ropa pero al revisar cuanto detergente tienes te das cuenta que te quedan {CantDetergente} unidades de detergente, decides ir a comprar mas detergente")
time.sleep(1)
print("Te dirijes a la tienda, y te acercas a la vendedora")
time.sleep(3)

print("Al llegar a la tienda, te das vueltas por la tienda sin encontrar el detergente")
print()
if CantDetergente<9:
    print(" Vendedora: ¿Viene a comprar detergente?")
    resp=input()
    if resp.lower()=="si":
        print("Vendedora: ¿Cuanto detergente va a comprar?")
        DetergenteComprado=int(input())
        CantDetergente+=DetergenteComprado
