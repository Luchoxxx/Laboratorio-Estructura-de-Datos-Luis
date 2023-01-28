
#Ejercicio 1  
variable = "LuisAlberto" 

def polindromo(cadena):
    cadenaPrueba = ""    
    contador= 0 

    longitudCadena = len(cadena) - 1 
    bandera = True

    while bandera:
        letra = cadena[longitudCadena - contador]
        contador = contador + 1
        cadenaPrueba = cadenaPrueba + letra
        
        if len(cadenaPrueba) == len(cadena) :
            break

    if cadenaPrueba == cadena :
        print("Es un polindromo")
    else:
        return "No es un polindromo"

print(polindromo(variable))

