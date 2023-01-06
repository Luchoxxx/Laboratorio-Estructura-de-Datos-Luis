

#Un robot puede dar pasos de 1 o 2 metros. 
# Escriba un programa para numerar todas las maneras en que el robot camina n metros.

def robot_camina(npasos):

    if npasos%2 == 0 :
        
        print(f"Camino { npasos /2}")
        
    else:
       if npasos%2 != 0 :
        print(f"camino { npasos}")

####Probar 

print(robot_camina(11))
print(robot_camina(12))







