
#EL MISMO EJERCICIO DE ROBOT QUE DA PASOS PERO ESTA VEZ PARA 1, 2 O 3 PASOS :

def robot_camina(npasos):
    
    if npasos == 1 or npasos ==2 : 

        return npasos
    
    elif npasos == 3:
        
        return npasos + 1

    return robot_camina(npasos - 1) + robot_camina(npasos  - 2) + robot_camina(npasos -3)
    
print(robot_camina(4))
print(robot_camina(1))
print(robot_camina(3))



