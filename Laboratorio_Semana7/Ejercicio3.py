

def divide_cadena(cadena):

    
    for letra in cadena :
        
        if letra == ",":
            
            return cadena.split()

print(divide_cadena("Luis,Alberto,Fernandez,Cardenas"))




