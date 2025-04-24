import time
num=int(input("Ingrese el numero para el temporizador: "))


while num>0:
    print(num)
    time.sleep(1)
    num-=1