
####COMENTARIO 1 #### 



####EJERCICO   2 ####
lista = [20,15,12,11,8,4,1]

contador = 0

for nota in lista:

    contador = contador + 1
    
    if contador == len(lista):
            print(nota)
    
    elif nota < lista[contador]:
        print(nota)


