
print("=======OPERACIONES DE CONJUNTOS=======")

mi_conjunto = {'Luis','Alberto','liz','karen','Roy'}
mi_conjunto1 = {'Luis','hafid','liz','Frank','Robert'}
mi_conjunto2 = {'Luis','jhosep','liz','Frank','Roberto'}


union = mi_conjunto|mi_conjunto1
union1 = union | mi_conjunto2
print(union1)

interseccion = mi_conjunto.intersection(mi_conjunto1).intersection(mi_conjunto2)
print(interseccion)

diferencia = mi_conjunto.difference(mi_conjunto1)
print(diferencia)   

diferencia_simetrica = mi_conjunto.symmetric_difference(mi_conjunto1)
print(diferencia_simetrica)








        

        
       









