'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e estrutura de dados

Autor:	Gabriel Cavalcati (gcm2)
Email:	gcm2@cin.ufpe.br
Data:	15/04/2018

Copyright(c) 2017 Gabriel Cavalcanti de Melo
'''
#__________________Lista_Duplamente_Encadeada__________________________
                    
class No():
    def __init__(self, valor = None, anterior = None, proximo = None):
        self.anterior = anterior
        self.valor = valor 
        self.prox = proximo
        
    def __repr__(self):
        return self.valor.__repr__()

    def __str__(self):
        return self.__repr__()
    
class Lista():
    def __init__(self):
        self.primeiro =  No()  
        self.ultimo = self.primeiro
        
        
    def listaVazia(self):
        '''Se a lista for vazia, retorna True. Se não, retorna False '''
        if self.primeiro == self.ultimo:
            return True
        return False
    
    def addFim(self,valor):
        '''Método para adicionar item no fim da lista.
        O ultimo será esse novo item q adicionaremos. Por isso,
        o nodo é criado com referencia anterior ao que antes era o ultimo, e
        o proximo será None'''
        self.ultimo.prox = No(valor, self.ultimo)
        self.ultimo = self.ultimo.prox
        
    def addInicio(self, valor):
        '''Método para adicionar no inicio. Nesse caso o primeiro item
        não será alterado, pois o primeiro item sempre será o nodo cabeça.
        Se lista for vazia, será a mesma coisa q adicionar no final'''
        if self.listaVazia():
            self.addFim(valor)
        else:
            self.primeiro.prox = No(valor, self.primeiro, self.primeiro.prox)
    
    def inserir(self, valor, indice):
        '''Método que adiciona o item em uma posição escolhida. Se a posiçao
        escolhida for igual a quantidade de itens na lista atual, será
        necessário, somente, adicionar no final. qNo outro caso, quando
        encontrada a posição desejada, é criado um novo nodo com referencias
        ao que está atualmente em sua posição e ao anterior a esse.'''
        if self.__len__() == indice or self.listaVazia():
            self.addFim(valor)
        else:
            cont=0
            aux = self.primeiro.prox
            while cont < indice:
                cont+=1
                aux = aux.prox
            aux.anterior = No(valor,aux.anterior,aux)
            aux.anterior.anterior.prox = aux.anterior


    def inserirOrdenado(self, valor):
        if self.listaVazia():
            self.addFim(valor)
            return
        aux = self.primeiro.prox
        while not aux.prox is None and (valor-aux.valor) >= 0:
            aux = aux.prox
        if aux.prox is None:
            if (valor-aux.valor) >= 0:
                self.addFim(valor)
                return
        aux.anterior = No(valor, aux.anterior, aux)
        aux.anterior.anterior.prox = aux.anterior
         
        


    def inverse(self):
        if self.listaVazia() or self.primeiro.prox is self.ultimo:
            return
        #tamanho = self.__len__()
        
        
        


    
    def __getitem__(self, indice):
        '''Método para pegar o item que esta localizado na posicao desejada '''
        aux = self.primeiro.prox
        cont = 0
        tamanho = self.__len__()
        if cont >= tamanho:
            return None
        while cont<tamanho:
            if cont==indice:
                return aux.valor
            aux = aux.prox
            cont+=1
            if aux is None:
                return None

    def __setitem__(self, indice, value):
        aux = self.primeiro.prox
        cont = 0
        tamanho = self.__len__()
        while cont<tamanho:
            if cont==indice:
                aux.valor = value
                return
            aux = aux.prox
            cont+=1
            if aux is None:
                return None
            
    def buscarItem(self, item):
        '''Método para buscar e retornar um item da lista '''
        aux = self.primeiro.prox
        while aux != None and aux.valor != item:
            aux = aux.prox
        return aux.valor

    def removerFim(self):
        '''Método para remover o ultimo item da lista. Nesse caso o ultimo
        elemente passará a ser o anterior ao antigo ultimo item'''
        if self.listaVazia():
            return None
        aux = self.ultimo
        self.ultimo = aux.anterior
        aux.anterior.prox = None
        del aux
        
        
    def removerInicio(self):
        '''Método para remover do inicio. Somente será preciso
        alterar asreferencias do primeiro e o anterior do do segundo item.
        Se a Lista tiver apenas um item, chama o metodo de remover o ultimo'''
        if self.listaVazia():
            return None
        aux = self.primeiro.prox
        if aux == self.ultimo:
            return self.removerFim()
        aux.prox.anterior = self.primeiro
        self.primeiro.prox = aux.prox
        del aux
                

    def removerItem(self, itemRemover):
        '''Percorremos a lista, procurando o item desejado. Caso não
        encontrar, não retorna nada. Caso encontre, altera as referencias
        dos vizinhos e deleta o atual'''
        aux = self.primeiro.prox
        while aux != None and aux.valor != itemRemover:
            aux = aux.prox
        if self.primeiro.prox == aux or self.ultimo == aux:
            return self.removerFim()
        if aux is None:
            return 
        aux.prox.anterior = aux.anterior
        aux.anterior.prox = aux.prox
        del aux

    def __len__(self):
        ''' Método especial que define o tamanho da lista'''
        cont = 0 
        aux = self.primeiro
        while aux.prox != None:
            cont+=1
            aux = aux.prox
        return cont
    
    '''
    def __iter__(self):
        return self

    def __next__(self):
        aux = self.primeiro.prox
        while aux.prox != None:
            return aux
            aux = aux.prox
    '''
               
    def __repr__(self):
        '''Método especial para representação da lista'''
        if self.listaVazia():
            return "[]"
        listaCompleta="["
        aux = self.primeiro.prox
        while aux.prox != None:
            listaCompleta +=aux.valor.__repr__()
            listaCompleta += ", "
            aux = aux.prox
        listaCompleta +=aux.valor.__repr__()
        listaCompleta+="]"
        return listaCompleta
        
            
            
    def __str__(self):            
        return self.__repr__()



