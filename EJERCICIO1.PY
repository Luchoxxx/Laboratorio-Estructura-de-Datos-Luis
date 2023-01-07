from random import randrange


#ALGORITMO DE DESORDEN:
#Primeros pasos

def desordena(cadena):
    elemento = len(cadena)  # cada elemento de la cadena 

    while elemento > 1 :
        elemento =  elemento - 1

        objeto = randrange(elemento)  # Generando numeros aleatorios de 0 a numeros de elementos
        
        #En esta parte estoy asignando a numero aleatorio que salga de anterir a la posicion y la igualo al elemto
        cadena[objeto]=  cadena[elemento]
        #Lo mismo que en la anterior linea .

        cadena[elemento] = cadena[objeto]
     
    return cadena 


##PRUEBA DE DESORDEN 
cadena_prueba = [1,2,3,4,5,6,7,8,8]
cadena_prueba1 = [1,2,2,2,5,6,7,7,7]
cadena_prueba2= [1,1,1,2,2,3,4,8,8]

print(desordena(cadena_prueba))
print(desordena(cadena_prueba1))
print(desordena(cadena_prueba2))





