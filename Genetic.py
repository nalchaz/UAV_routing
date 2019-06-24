# @author : Nahel Chazot
# Genetic algorithm for TSP problem

from Classes.solution import Solution
from Classes.population import Population

def generateRandomSolution(prob):
	sol = Solution()
	sol.generateRandomSolution(prob)
	return sol

def generateRandomPopulation(prob, size):
	pop = Population()

	for i in range(0, size):
		sol = generateRandomSolution(prob)
		pop.addElement(sol)

	return pop


