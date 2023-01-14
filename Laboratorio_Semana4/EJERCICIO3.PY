##Funcion que crea un arry##

tamaño_lista = int(input("Indique el tamaño de lista: "))
mi_numero = int(input("Ingresa un numero: "))

def Crea_Lista(tamaño_lista,mi_numero):

    lista_multiplos = []
    lista_numeros = []
    contador = 0

    for numero in range(tamaño_lista):
        contador = contador + 1
        lista_numeros.append(contador)
        
        for num in lista_numeros:
            multiplo = num * mi_numero
            
        lista_multiplos.append(multiplo)
        
    return lista_multiplos

##FUNCION DE LOS MULTIPLOS ##### 

print(Crea_Lista(tamaño_lista,mi_numero))









