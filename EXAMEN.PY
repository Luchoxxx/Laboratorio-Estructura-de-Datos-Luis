
####PREGUNTA 1 ##### 


numero_n = int(input("Ingrese un numero: "))
numero_p = int(input("Ingrese un numero: "))

def sumatoria(numero_n,numero_p):

    if numero_n == 1:
        return numero_p
    
    else:
        return (numero_p*numero_n) + sumatoria(numero_n +1, numero_p)

suma_prueba = sumatoria(numero_n,numero_p)

print(suma_prueba)











