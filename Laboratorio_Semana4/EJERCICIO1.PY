
print("======EJERCICIO 1 ======")

def acumulador(contador):
    
    list_lobgitud = []
    lista_nombres = []
    
    while len(lista_nombres) < contador :
        
        nombre = input("Ingresa tu nombre: ")

        lista_nombres.append(nombre)
        list_lobgitud.append(len(nombre))   ###O(n) ---> O(n) 

        if len(lista_nombres)== contador:
            break
        
    return lista_nombres , list_lobgitud
        
prueba = acumulador(3)
print(prueba)

###






