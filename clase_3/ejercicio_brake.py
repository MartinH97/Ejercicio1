cantidad= 0
num= int(input("numero: "))
while num != 0:
    primo=True 
    for i in range(2,num):
        if num%i==0:
            primo=False
            break
    if primo:
        cantidad+=1
    num= int(input("Numero:"))
print(f"Primos: {cantidad}")           



