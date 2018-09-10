class Node():
	def __init__(self,item = None, previus_node = None, next_node = None):
		self.item = item
		self.previus_node = previus_node
		self.next_node = next_node

	def __str__(self):
		return str(self.item)

	def __repr__(self):
		return self.__str__()

class List():
	def __init__(self, *item = None):
		self.len = 0
		if item is None:
			self.head = Node() = self.tail
		else:
			aux = self.head
			for x in item:
				aux.next_node = Node(x,aux)
				aux = aux.next_node
				self.len += 1
			self.tail = aux

	def empty(self):
		if self.head == self.tail:
			return True
		return False

	def __len__(self):
		return self.len

	def append(self, item):
		self.tail.next_node = Node(item,self.tail)
		self.tail = self.tail.next_node

	def pop(self, index):
		cont = 0
		aux = self.head.next_node
		if index >= self.__len__():
			index = self.__len__() - 1
		while cont < index:
			aux = aux.next_node
			cont+=1
		if cont == self.__len__():
			aux.previus_node.next_node = aux.next_node
			return aux
		aux.previus_node.next_node = aux.next_node
		aux.next_node.previus_node = aux.previus_node
			





		