import time
# EJERCICIO DE EL FACTORIAL DE UN NUMERO:

#MANERA NORMAL
def factorial(n):
    inicio = time.time()
    resultado = 1
    contador = 0

    while contador < n :

        contador = contador + 1 
        resultado = resultado * contador
    final  = time.time()
    return print(f'El tiempo de ejecucion fue {final- inicio} ===> resultado: {resultado}')

#variable = factorial(4)

# print(variable)
# print(factorial(5))
# print(factorial(6))

#MANERA RECURSIVA 

def factorial_recursivo(numero):
    inicio = time.time()

    if numero == 1:
        return numero

    final = time.time()

    tiempo = final - inicio
    return numero*factorial_recursivo(numero - 1) , tiempo
    

### PRUEBA
 
varible2 = factorial(10)
varible1 = factorial_recursivo(10)

print(varible1)
print(varible2)



