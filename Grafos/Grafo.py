###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:	Gabriel Cavalcanti 
# Email:	gcm2@cin.ufpe.br
# Data:		2018-06-10
#
# Licenca: The MIT License (MIT)
#			Copyright(c) 2018 Gabriel Cavalcanti
#
###############################################################################

class Grafo():
    def __init__(self, v, direcionado=False, peso=False):
        self.__vertices = v
        self.__arestas = 0
        self.__direcionado = direcionado
        self.__peso = peso
        self.__adj = []
        for i in range(v):self.__adj.append([])

    def getAdj(self, v):
        '''retorna a lista de adjacentes de um vertice'''
        return self.__adj[v]

    def getArestas(self):
        '''retorna a quantidade de arestas do grafo'''
        return self.__arestas

    def direcionado(self):
        '''retorna se o grafo e direcionado ou nao'''
        return self.__direcionado
        
    def peso(self):
        '''retorna se o grafo tem peso nas arestas ou nao'''
        return self.__peso

    def __len__(self):
        '''retorna a quantidade de vertices do grafo'''
        return self.__vertices


    def inserirAresta(self, u, v, peso = 1):
        '''Insercao de arestas no grafo. Se algum dos vertices pedidos
        nao existir no grafo, retorna erro. Se tiver peso, checa o primeiro
        item da tupla que contem o adjacente e o peso da aresta'''
        if v < self.__vertices and u < self.__vertices:
            if self.peso():
                for x in self.__adj[u]:
                    if x[0]==v:
                        raise KeyError
                self.__adj[u].append((v,peso))
                if not self.direcionado():
                    self.__adj[v].append((u,peso))
                    
            else:
                if v not in self.__adj[u]:
                    self.__adj[u].append(v)
                    if not self.direcionado():
                        self.__adj[v].append(u)
        else:
            raise KeyError

        

    def removerAresta(self,u, v):
        '''Remove a aresta que liga os dois veertices. Se for direcionado
        só tira a aresta que liga o primeiro ao segundo'''
        if not self.peso():
            if v in self.__adj[u]:
                self.__adj[u].remove(v)
                if not self.direcionado():
                    self.__adj[v].remove(u)
            else: raise KeyError
        else:
            for x in self.__adj[u]:
                if x[0] == v:
                    self.__adj[u].remove(x)
                    if not self.direcionado():
                        for x in self.__adj[v]:
                            if x[0]==u: self.__adj[v].remove(x)

    def existe(self, u, v):
        '''verifica se existe algma arresta que liga dois vertices'''
        if self.peso():
            for x in self.__adj[u]:
                if x[0]==v:
                    return True
            if self.direcionado():
                for x in self.__adj[v]:
                    if x[0]==u:
                        return True
            return False
        if v in self.__adj[u] or u in self.__adj[v]:
            return True
        return False


    def grauEntrada(self, v):
        '''retorna quantos vertices tem v como adjacente'''
        grau = 0
        if not self.peso():
            for x in self.__adj:
                for i in x:
                    if i==v:
                        grau+=1
        else:
            for x in self.__adj:
                for i in x:
                    if i[0]==v:
                        grau+=1
        return grau

    def grauSaida(self, v):
        '''retorna a quantidade de adjacente de um vertice'''
        return len(self.__adj[v])




                
            
        
        
        



    

    
