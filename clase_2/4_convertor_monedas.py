mensaje= """
Hola, este es un conversor de monedas:
1- Soles - Dolares
2- Euros - Dolares
3- Pesos Colombianos - Dolares
"""
print(mensaje)
opcion= int(input("Ingrese la opcion que desee realizar:"))

if opcion == 1:
     tipo_cambio = 0.28
     convertir = float(input("Ingrese el monto que desee cambiar: "))
     convertir = convertir*tipo_cambio
     print(f"El cambio de Soles a Dolares es de: {convertir:.2f}")
elif opcion == 2:
     tipo_cambio = 1.09
     convertir = float(input("Ingrese el monto que desee cambiar: "))
     convertir = convertir*tipo_cambio
     print(f"El cambio de Euros a Dolares es de: {convertir:.2f}")
elif opcion == 3:
     tipo_cambio = 0.00027
     convertir= float(input("Ingrese el monto que desee cambiar: "))
     convertir= convertir*tipo_cambio
     print(f"El cambio de Pesos Colombianos a Dolares es de: {convertir:.2f}")