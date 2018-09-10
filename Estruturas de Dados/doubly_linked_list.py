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
	def __init__(self, item = None):
		if item is None:
			self.head = Node() = self.tail
		else:
			pass


		