def leer_frase():
    global txt
    txt=(input("Ingrese un texto: "))
def contar_letras():
    conta=0
    for i in txt:
        if(i.isalpha()):
            conta+=1
    print("La cantidad de letras son", conta)
    
leer_frase()
contar_letras()
    