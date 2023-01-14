
print("==========Programa multiplos de un numero==========")
def multiplo_num():
    numero = int(input("\nIndique el numero a devolver los multiplos: "))
    tamano = int(input("Indique el tamaño de la lista: "))

    lista = []
    num_naturales = []
    contador = 0

    for i in range(tamano):
        contador = contador + 1
        num_naturales.append(contador)

        for x in num_naturales:
            multiplos = x * numero

        lista.append(multiplos)

    print(f"Los multilpos de {numero} son: ", lista)

multiplo_num()