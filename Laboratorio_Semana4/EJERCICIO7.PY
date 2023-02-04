###MULTIPLICACION DE MATRICES ###

matrizA =[[1,2,3],
         [4,5,6],
         [7,8,9]]

matrizB =[[2,2,3],
         [6,0,3],
         [7,7,0]]

def multiplicacion_matrices(matrizA,matrizB):

    if len(matrizA[0]) != len(matrizB[0]):
        return "Las matrices no se puden multiplicar"

    resultado = [[0 for j in range(len(matrizB[0]))]]

print(multiplicacion_matrices(matrizA, matrizB))

print("Hola")




