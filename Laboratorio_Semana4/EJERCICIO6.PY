
###SUMA DE MATRICES ##### 

matrizA =[[1,2,3],
         [4,5,6],
         [7,8,9]]

matrizB =[[2,2,3],
         [6,0,3],
         [7,7,0]]

def suma_matrices(matrizA,matrizB):

    if len(matrizA) != len(matrizB) or len(matrizA[0] != len(matrizB[0])):
        return "Las matrises no son del mismo orden"


    resultado = [[o for j in range(len(matrizA[0]))] for i in range(len(matrizA))]

    for i in range(len(matrizA)):

        for j in range(len(matrizA[0])):

            resultado[i][j] = matrizA[i][j] + matrizB[i][j]

    return resultado 






