

def frecuencia(cadena):

    frecuencia = {}

    for letra in cadena:

        if letra in frecuencia :

            frecuencia[letra] += 1
        
        else:
            frecuencia[letra] = 1
    
    return frecuencia 

cadena = "LuisAlbertoFernandez"
print(frecuencia(cadena))




