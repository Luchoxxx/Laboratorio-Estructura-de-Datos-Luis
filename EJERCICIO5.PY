
#NUMEROS DE FOBONACI

#De manera recursiva :

def fibonaci_recursivo(numero):
    if numero == 0:
        return 1
    
    elif numero == 1:
        return 1
    else:
        return fibonaci_recursivo(n-1) + fibonaci_recursivo(n-2)

print(fibonaci_recursivo(10))

# PARA UN AMANERA NORMAL

def fibonaci_N(numero):
    
    contador = 0
    resultado = []
    while contador < numero :

        contador = contador + 1 

        if numero== numero -1 :

            resultado.append(numero -1)

        elif numero == numero -2:

            resultado.append(numero - 2)
    return resultado

print(fibonaci_N(5))
