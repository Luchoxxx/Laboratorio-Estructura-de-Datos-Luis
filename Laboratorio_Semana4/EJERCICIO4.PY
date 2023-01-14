
def leer_vector(vector):
    for i in range(len(vector)):

        if sum(vector[:i] + vector[i+1:]) == vector[i]:
            return True
            
    return False

vector = [1, 2, 3, 4, 10]

if leer_vector(vector):
    print("Hay un número que es igual a la suma de los demás elementos del vector.")
else:
    print("No hay un número que sea igual a la suma de los demás elementos del vector.")

