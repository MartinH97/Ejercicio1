num1= int(input("Ingrese un numero: "))
num2= int(input("Ingrese otro numero: "))
num3= int(input("Ingrese otro numero: "))
num4= int(input("Ingrese otro numero: "))
## 
if num1>num2>num3>num4:
    print(f"El numero mayor es {num1}")
elif num2>num1>num3>num4:
    print(f"El numero mayor es {num2}")
elif num3>num2>num1>num4:
    print(f"El numero mayor es {num3}")
elif num4>num3>num2>num1:
    print(f"El numero mayor es {num4}")
if num1<num2<num3<num4:
    print(f"El numero menor es {num1}")
elif num2<num1<num3<num4:
    print(f"El numero menor es {num2}")
elif num3<num2<num1<num4:
    print(f"El numero menor es {num3}")
elif num4<num3<num2<num1:
    print(f"El numero menor es {num4}")    