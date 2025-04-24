clave=1904
intentos=3
password=int(input("Ingresa tu clave:"))

while clave!=password and intentos>0:
    print("Contraseña incorrecta")
    intentos-=1
    print(f"ERROR, le quedan {intentos} intentos.")
    if intentos<=0:
        break
    else:
         password=intpassword=int(input("Ingresa tu clave:"))

if clave==password:
     print("Log in exitoso")
elif clave!=password:
      print("Sistema bloqueado")
