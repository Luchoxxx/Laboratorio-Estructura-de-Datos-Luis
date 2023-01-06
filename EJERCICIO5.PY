
#NUMEROS DE FOBONACI

#De manera recursiva :

def fibonaci(numero):

    if numero == 1:
        return 1 

    elif numero == 2 :
        return 2 
    else:
        return fibonaci(numero -1 ) + fibonaci(numero -2)

def fibonaci(numero):

    contador = 0
    
    while contador < numero :
        contador = contador + 1 
        
