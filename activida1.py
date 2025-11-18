#LR-2024-02270 JUAN MERCEDES

nombre = input("Ingrese el nombre, x favor: ")
edad = int(input(f"{nombre} Ingresa tu edad (obviamente que sea mas de 0): "))

if edad >= 18:
    print(f"\n El usuario {nombre} es mayor de edad. \n")
elif edad <= 0:
    print("\n AHHH, " + nombre + " ¿te crees gracioso? \n")
else:
    print(nombre, " eres menor de edad. \n")
    
continuar = "s"
    

while continuar == "s":
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))

    if num2 > 0:
        print(f"\n{num1} +  {num2} = {num1+num2}")
        print(f"{num1} -  {num2} = {num1-num2}")
        print(f"{num1} x  {num2} = {num1*num2}")
        print(f"{num1} ÷  {num2} = {num1/num2}\n")
    else:
        print(f"\n{num1} +  {num2} = {num1+num2}")
        print(f"{num1} -  {num2} = {num1-num2}")
        print(f"{num1} x  {num2} = {num1*num2}")
        print(f"ERROR, el divisor no puede ser 0.")
    
    
    numero_secreto = num1+num2
    repuesta = int()
    
    while repuesta != numero_secreto:
        repuesta = int(input("Adivina el numero secreto: "))
        if repuesta > numero_secreto:
            print("Fallaste, el numero es mas pequeño")
        elif repuesta < numero_secreto:
            print('Fallaste, El numero es mas alto. "Una pista: Ya lo has visto recientemente."')
        else:    
            print(f"\n Felicidade adivinaste el numero secreto, que era: {num1+num2}\n")
            
    continuar = input('Desea continuar Juagando:  "s" para si y "n" para no: ')
    
print("\nGracias por Jugar. ")
 
