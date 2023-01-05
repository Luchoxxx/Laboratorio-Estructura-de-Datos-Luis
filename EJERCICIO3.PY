
#EJERCICIO 3 

#Creamos una funcion de ordenamiento 

def orden(lista):
#Recorremos todos los elemtos de la lista

    for elemento in range(len(lista)):

        #Decimos que mi primer elemto es es mas pequeño
        elemento_pequeño =  elemento

        #Estoy recorriendo ese misma lista asia la derecha

        for objeto  in range(elemento +1 , len(lista)):

            #Ponemos una condicional para cuando encuentre un elemto pequeño
            if lista[objeto] < lista[elemento_pequeño]:

                elemento_pequeño = objeto

        if elemento_pequeño != elemento:
            
            lista[elemento] , lista[elemento_pequeño] = lista[elemento_pequeño], lista[elemento]

lista = [2,4,1,1,4,6,8,2,5]

orden(lista)

print(lista)










