import random
import Utils

class Solution:

	def __init__(self):
		self.sol = [] # vector solution
		self.cost = 0 

	def generateRandomSolution(self, prob):
		for i in range(len(prob.x)):
			self.sol = self.sol + [i]

		random.shuffle(self.sol)
		self.cost = Utils.DisTotal(self.sol, prob)

	def calculateCost(self, prob):
		self.cost = Utils.DisTotal(self.sol, prob)

	def copy(self):
		copy = type(self)
		copy.sol = self.sol
		copy.cost = self.cost
		return copy

	def __str__(self):
		# return str(self.sol) + " Cost : " + str(self.cost)
		return " Cost : " + str(self.cost)

	def __eq__(self, other):
		return self.sol == other.sol

	def __hash__(self):
		return hash('.'.join(str(x) for x in self.sol))

	