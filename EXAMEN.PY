
####PREGUNTA 1 ##### 


numero_n = int(input("Ingrese un numero: "))
numero_p = int(input("Ingrese un numero: "))

def sumatoria(numero_n,numero_p):

    if numero_n == 1:
        return numero_p
    
    else:
        return numero_p*numero_n + sumatoria(numero_n - 1, numero_p)

suma_prueba = sumatoria(numero_n,numero_p)

print(f'La suma rescursiva de {numero_n} y {numero_p}  es {suma_prueba}')



#####PREGUNTA 2 ####


def decimal_hexadecimal(numero):

  if numero == 0:
    return 0
  else:
    return str(decimal_hexadecimal(numero // 16)) + str(numero % 16).upper()

##PRUEBA #### 
prueba1 = decimal_hexadecimal(8642)


####PREGUNTA 3 #### 

numero = int(input("Imgrese un numero: "))
base = int(input("Ingrese la base: "))

def trasformador(a , b ):

    if a == 0:
        return "0"

    residuo = a % b 

    respuesta = trasformador(a//b, b)

    return respuesta + str(residuo)
###PRUEBA ###

prueba = trasformador(numero, base)

print(prueba)






