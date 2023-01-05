
# EJERCICIO DE EL FACTORIAL DE UN NUMERO:

def factorial(n):

    resultado = 1
    contador = 0

    while contador < n :

        contador = contador + 1 
        resultado = resultado * contador
         
    return resultado

variable = factorial(4)

print(variable)
print(factorial(5))
print(factorial(6))


