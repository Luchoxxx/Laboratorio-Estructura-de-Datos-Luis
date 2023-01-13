
def multiplos(numero):

    lista = []

    if numero == 1:
        return numero
    else:
        lista.append(numero*multiplos((numero -1)))

    return lista 

multipl= multiplos(4)
print(multipl)
 
 