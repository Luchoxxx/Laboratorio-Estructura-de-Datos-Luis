

##Funcion que crea un arry 

def Crea_Lista():

    tamaño_lista = int(input("Indique el tamaño de lista: "))
    mi_numero = int(input("Ingresa un numero: "))
        
        #FUNCION DE LOS MULTIPLOS 
    def funcion_multiplos(mi_numero,tamaño_lista):
        lista_multiplos = []

        for multiplo in range(1,tamaño_lista + 1):

            if multiplo%mi_numero == 0:
                lista_multiplos.append(multiplo)

        return lista_multiplos


    lista_creada = []
    while len(lista_creada) <= tamaño_lista :
        lista_creada.append(funcion_multiplos(mi_numero, tamaño_lista))
    
    return lista_creada 

##FUNCION DE LOS MULTIPLOS ##### 

    


prueba = Crea_Lista() 

print(prueba)




