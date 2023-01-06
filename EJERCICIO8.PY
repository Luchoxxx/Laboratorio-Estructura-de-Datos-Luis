
#PROGRAMA RECURSIVO DE LA POTENCIA 

def potencia_numero(numero , potencia):

    if potencia ==  0 :
        return 1
    else:
        return numero * potencia_numero(numero , potencia -1)

print(potencia_numero(3, 3))


