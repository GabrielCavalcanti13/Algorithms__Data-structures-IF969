'''
 Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
 Centro de Informatica -- CIn (http://www.cin.ufpe.br)
 Bacharelado em Sistemas de Informacao
 IF969 -- Algoritmos e Estruturas de Dados

 Autor:	Renato Vimiero/Gabriel Cavalcanti
 Email:	gcm2@cin.ufpe.br
 Data:	 2018-03-11

 Descricao: O programa cronometra o tempo gasto para percorrer um vetor de
 tamanho N, com finalidade de achar triplas que somadas resultam ZERO.

 Licenca: The MIT License (MIT)
			Copyright(c) 2018 Gabriel Cavalcanti de Melo
'''


import sys
from time import perf_counter
import numpy

MAX = 999999

class Cronometro:
   ''' Cronometra tempo gasto desde a criacao ate a chamada do metodo
       tempo_gasto
   '''    
   def __init__(self):
      self.__criacao = perf_counter()
   def tempo_gasto(self):
      return perf_counter() - self.__criacao

def gera_seq_aleatoria(tam):
   return numpy.random.randint(-MAX,MAX, size=tam)

def conta_somas(vetor):
   '''Conta quantas triplas que somadas resultam em zero. Faz isso varrendo o
vetor usando tres variaveis(x,y,z),que vao representar cada elemento da tripla
parando quando chegar na ultima tripla do vetor '''
   total=0
   for x in range(len(vetor)):
      if x<=len(vetor)-3:
         for y in  range(x+1, len(vetor)):
            for z in range(y+1, len(vetor)):
               if vetor[x]+vetor[y]+vetor[z] == 0:
                  total+=1
   return total

def main():
	'''
	Contem os comandos em Python referentes `a implementacao do algoritmo
	'''
	seeds = [11,7,13,19,5189]
	tam = [50,100,250,500,1000]
	for i,seed in enumerate(seeds):
	   numpy.random.seed(seed)
	   vetor = gera_seq_aleatoria(tam[i])
	   cron = Cronometro()
	   total = conta_somas(vetor)
	   print(total)
	   print("Tempo gasto com {0} elementos foi {1} segundos".format(tam[i],cron.tempo_gasto()))
	   del vetor
	   del cron


if __name__ == '__main__':
	main()
