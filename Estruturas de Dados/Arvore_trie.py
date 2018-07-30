###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:	Gabriel Cavalcanti de Melo
# Email:	gcm2@cin.ufpe.br
# Data:		2018-05-15
#
# Descricao:  Arvore trie, que otimiza a busca de elementos, usando prefixos 
#
# Licenca: The MIT License (MIT)
#			Copyright(c) 2018 Gabriel Cavalcanti
#
###############################################################################

class No():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.filho = [None]*10

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.__repr__()



class Indice():
    def __init__(self):
        self.__raiz = No()
        self.__tamanho = 0

    def inserir(self, chave, valor):
        '''Insere elemento na arvore trie. Checa se já existe um elemento
        com mesma chave. Se ja existir, substitui e não aumenta o tamanho
        da arvore '''
        nodo = self.__raiz
        for x in chave:
            if nodo.filho[int(x)] is None:
                nodo.filho[int(x)] = No(x)
            nodo = nodo.filho[int(x)]
        if nodo.value is None:
            nodo.value = valor
            self.__tamanho += 1
            return
        nodo.value = valor
        

    def buscar(self, chave):
        '''Busca elemento na lista a partir de sua chave'''
        nodo = self.__raiz
        for x in chave:
            if nodo.filho[int(x)] is None:
                raise KeyError
            nodo = nodo.filho[int(x)]
        if not nodo.value is None:
            return nodo.value
        raise KeyError


    def __getitem__(self, chave):
        '''Metodo especial que permite a busca usando colchetes como em:
        trie[chave]'''
        return self.buscar(chave)
    

    def __setitem__(self, chave, valor):
        ''' Metodo especial permite adicionar ou modificar um elemento na
        arvore. trie[chave] = valor'''
        self.inserir(chave, valor)
        
        
    def __len__(self):
        '''Metodo que retorna a quantidade de nodos com valores contidos
        na arvore'''
        self.__tamanho
        
        
