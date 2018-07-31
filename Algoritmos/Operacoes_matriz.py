###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:	Gabriel Cavalcanti 
# Email:	gcm2@cin.ufpe.br
# Data:		2018-05-30
#
# Licenca: The MIT License (MIT)
#			Copyright(c) 2018 Gabriel Cavalcanti
#
###############################################################################
def transposta(matriz):
    matrizTransposta = []
    cont = 0
    tam = len(matriz)
    for x in range(tam):
        new = []
        for z in matriz:
            new.append(z[x])
        matrizTransposta.append(new)
    return matrizTransposta

def multiplicar_matriz(matriz1, matriz2):
    newMatriz = []
    for i in matriz1:
        newLine = []
        for j in range(len(matriz2)):
            result = 0
            #multiplicacao de linha por coluna
            for x in range(len(i)):
                result+=i[x]*matriz2[x][j]
            newLine.append(result)
        newMatriz.append(newLine)
    return newMatriz

if __name__ == '__main__':
    lista1 = [[1,2],[3,4]]
    lista2 = [[-1,4],[3,2]]
    newLista2 = transposta(lista2)
    print("A transposta de "+str(lista2)+" eh:\n"+str(newLista2)+"\n")
    a = multiplicar_matriz(lista1,newLista2)
    print("O resultado da multiplicacao das duas matrizes é:\n"+str(a))








            
        
             
    
