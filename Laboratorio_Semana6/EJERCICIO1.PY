
print("=======OPERACIONES DE CONJUNTOS=======")

mi_conjunto = {'Luis','Alberto','liz','karen','Roy'}
mi_conjunto1 = {'Luis','hafid','liz','Frank','Robert'}
mi_conjunto2 = {'Lucho','jhosep','liz','Frank','Roberto'}


union = mi_conjunto.union(mi_conjunto1)
print(union)

interseccion = mi_conjunto.intersection(mi_conjunto1)
print(interseccion)

diferencia = mi_conjunto.difference(mi_conjunto1)
print(diferencia)

###La diferencia simetrica de los tres conjuntos #### 

diferencia3 = (mi_conjunto.difference(mi_conjunto1)).difference(mi_conjunto2)

print(diferencia3)






