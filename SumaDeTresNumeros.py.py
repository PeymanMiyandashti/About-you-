#Peyman Miyandashti 250161 
#resta de 2 numeros con if elif else 
# Pedir al usuario que ingrese dos números
num1=int(input("ingrese el primer numero:"))
num2=int(input("ingrese el segundo numero:"))

# Display the two subtraction options
print("\nElige una opción:")
print("1: num1 - num2 =", num1, "-", num2)
print("2: num2 - num1 =", num2, "-", num1)

# Pide a la usuaria que elija una opción.
opcion = input("engresar opcion 1 or 2: ")

# Realizar la resta seleccionada
if opcion == "1":
    result = num1 - num2
    print("\nResultado: num1 - num2 =", result)
elif opcion == "2":
    result = num2 - num1
    print("\nResultado: num2 - num1 =", result)
else:
    print("\nInvalido opcion seleccionada.") 
#fin