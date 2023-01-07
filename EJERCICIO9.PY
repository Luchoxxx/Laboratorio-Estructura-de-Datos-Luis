
# Suma recursiva 


def suma_recursiva(a,b):

    if b== 0:
        return a 
    
    else:
        return suma_recursiva(a, b - 1) + 1

##PRUEBA 

suma_recursiva(1, 5)

    










