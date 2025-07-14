#peyman Miyandashti 250161
#maximo 3 numeros 
num1=float(input("ingrese el primer numero:"))
num2=float(input("ingrese el segundo numero:"))
num3=float(input("ingrese el tercero numero:"))

if num1>num2:
    if num1>num3:
        max=num1
    else:
        max=num3
else:
    if num2>num3:
        max=num2
    else:
        max=num3

print(f"el numero mayor es :{max}")