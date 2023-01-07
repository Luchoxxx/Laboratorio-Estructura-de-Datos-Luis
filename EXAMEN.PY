
####PREGUNTA 1 ##### 


numero_n = input(int("Ingrese un numero:"))
numero_p = input(int("Ingrese un numero:"))

def sumatoria(numero_n,numero_p):

    if numero_n == 1:
        return numero_p
    
    else:
        return numero_p*numero_n + sumatoria(numero_n +1, numero_p)












