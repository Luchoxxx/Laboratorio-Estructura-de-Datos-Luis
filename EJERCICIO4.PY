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
    final = time.time()
    
    return resultado , final - inicio  
   # return print(f'El tiempo de ejecucion fue {final- inicio} ===> resultado: {resultado}')

#variable = factorial(4)

# print(variable)
# print(factorial(5))
# print(factorial(6))

#MANERA RECURSIVA 

inicio = time.time()

def factorial_recursivo(numero):
    

    if numero == 1 :    
        return  1

 #   final = time.time()

    return numero*factorial_recursivo(numero - 1)
final = time.time()


### PRUEBA
 
print(factorial(10))
print(factorial_recursivo(10))
print(final - inicio)





