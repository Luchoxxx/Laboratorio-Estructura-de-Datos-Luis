
def longitud_subCadena(cadena):

    len_max = 0 
    concu_len = 0 
    for letra in cadena :

        if letra.isdigit():
            concu_len += 1 

        else:
            len_max = max(len_max, concu_len)

    return max(len_max, concu_len)

cadena = "123abc456def789"
print(longitud_subCadena(cadena))


