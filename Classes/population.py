import bisect

class Population:

	def __init__(self):
		self.elements = []
		self.hashElements = []

	def addElement(self, elem):
		if hash(elem) in self.hashElements:
			return False
		else:
			self.elements.append(elem)
			self.hashElements.append(hash(elem))
			self.elements.sort(key = lambda x: x.cost)
			return True


	def __str__(self):
		stri = []
		for i in range(0, len(self.elements)):
			stri.append(str(self.elements[i]))
			stri.append('\n')

		return ''.join(stri)