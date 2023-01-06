

#Un robot puede dar pasos de 1 o 2 metros. 
# Escriba un programa para numerar todas las maneras en que el robot camina n metros.


def robot_camina(npasos):
    
    if npasos== 1 or npasos==2:

        return npasos

    return robot_camina(npasos - 1) + robot_camina(npasos  - 2 )
    
print(robot_camina(4)) # 5 





