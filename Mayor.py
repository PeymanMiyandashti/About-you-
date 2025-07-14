#Peyman Miyandashti 250161
#La Differencia de numero 
num1=float(input("ingrese el primer numero:"))
num2=float(input("ingrese el segundo numero:"))
resta=num1-num2
if resta<=0:
    
    resta*=-1
print(f"La diferencia es {resta:.0f}")