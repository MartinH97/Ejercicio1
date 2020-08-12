mensaje= """
Hola!, que opcion desea realizar:
1- Area Cuadrado
2- Perimetro Rectangulo
"""
print(mensaje)
oper= int(input("Elija la opcion: "))
##
if oper == 1:
    lado= float(input("Ingrese el lado del cuadrado: ")) 
    result= lado*lado
    print(f"El resultado del area es: {result:.2f}")
elif oper == 2:
    lado= float(input("Ingrese el lado del cuadrado: ")) 
    result= lado*lado 
    print(f"El resultado del perimetro es: {result:.2f}") 
