# Forma 1 de contar caracteres

# frase=input("ingresa tu frase: ")
# cont=0
# for i in frase:
#     cont+=1
# print (f"La cantidad de caracteres es {cont}")

# Forma 2 de contar caracteres

# frase=input("ingresa tu frase: ")
# cont=len(frase)
# print (f"La cantidad de caracteres es {cont}")

# Forma 3 de contar caracteres

# frase=input("ingresa tu frase: ")
# print("La cantidad de caracteres es:",len(frase))

# frase=input("ingresa tu frase: ")
# contc=0
# contv=0
# for i in frase:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         contv+=1
#     else:
#         contc+=1
        
# print (f"La cantidad de VOCALES es {contv} Y CONSONANTES es {contc}")

# Forma 4 de contar caracteres

frase=input("ingresa tu frase: ")
cantcar=0
vo=0
cons=0
for i in frase:
    print(i)
    cantcar+=1
    if i.lower() in ("aeiou"):
        vo+=1
    elif i==" ":
       cantcar-=1
    else:
        cons+=1

print(f"La cantidad de CARACTERES es {cantcar}")
print (f"La cantidad de VOCALES es {vo} Y CONSONANTES es {cons}")