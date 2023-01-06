
#NUMEROS DE FOBONACI

def fibonaci(n):

    contador = 1
    resultado = 0 

    while contador <= n :
        
        contador = contador + 1 
        
        resultado = (n-1) + (n-2)
    return resultado

print(fibonaci(4))



