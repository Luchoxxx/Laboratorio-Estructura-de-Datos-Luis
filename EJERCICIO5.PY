import time
#NUMEROS DE FOBONACI

#De manera recursiva : 

def fibonaci_recursivo(numero):
    if numero == 0:
        return 1
    
    elif numero == 1:
        return 1
    else:
        return fibonaci_recursivo(numero-1) + fibonaci_recursivo(numero-2)

print(fibonaci_recursivo(10))

# PARA UN AMANERA NORMAL

def fibonaci_N(numero):
    
    lista = [0,1]

    if numero== 1:
        print('0')
    elif numero == 2:
        print('[0,1]')
    
    else:
        while len(lista) <numero :
            lista.append(0)

        if (numero==0 or numero == 1):
            
            return 1 
        else:
            lista[0]= 0 
            lista[1] = 1 

            for i in range(2, numero):

                lista[i] = lista[ i - 1] + lista[ i - 2] 

            print(lista)
    
####Probando 

print(fibonaci_N(10))

print(fibonaci_N(5))
