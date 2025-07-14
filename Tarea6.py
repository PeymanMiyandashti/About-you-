#Peyman Miyandashti 250161
#una tienda de abastos oferce un descuento del 8% sobre el total  de la compra y un cliente desea saber cuanto debera pagar finalmente por su compra , elabore un pseudocodigo y flujograma que resuelva este problema
#Pseudocódigo
#Inicio
  # Definir totalCompra, descuento, totalPagar como Real
   #Escribir "Ingrese el total de la compra:"
   #Leer totalCompra
   #descuento ← totalCompra * 0.08
   #totalPagar ← totalCompra - descuento
   #Escribir "El total a pagar con descuento es:", totalPagar
#Fin
# Solicitar al usuario el total de la compra
total_compra = float(input("Ingrese el total de la compra: "))

# Calcular el descuento del 8%
descuento = total_compra * 0.08

# Calcular el total a pagar
total_pagar = total_compra - descuento

# Mostrar el resultado
print("El total a pagar con el 8 % de descuento es:", total_pagar)