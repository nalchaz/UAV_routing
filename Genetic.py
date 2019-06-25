# @author : Nahel Chazot
# Genetic algorithm for TSP problem

import random

from Classes.solution import Solution
from Classes.population import Population
import LocalSearch
def generateRandomSolution(prob):
	sol = Solution()
	sol.generateRandomSolution(prob)
	return sol

def generateRandomPopulation(prob, size):
	pop = Population()

	for i in range(0, size):
		sol = generateRandomSolution(prob)
		LocalSearch.globalLocalSearch(sol, prob)
		while pop.exist(sol):
			sol = generateRandomSolution(prob)
			LocalSearch.globalLocalSearch(sol, prob)
		pop.addElement(sol)

	return pop

def mixWithRandomSolutions(prob, pop):
	for i in range(int(len(pop)/2), len(pop)):
		sol = generateRandomSolution(prob)
		LocalSearch.globalLocalSearch(sol, prob)
		while pop.exist(sol):
			sol = generateRandomSolution(prob)
			LocalSearch.globalLocalSearch(sol, prob)
		pop.elements[i]= sol

	return pop

def generateChild(prob, pop):

	rand1 = random.randint(0, len(pop.elements)*8/10)						#Element in the first 80% of the population
	rand2 = random.randint(len(pop.elements)*8/10+1, len(pop.elements)-1)		#Element in the last 20% of the population

	parent1 = pop.elements[rand1]
	parent2 = pop.elements[rand2]

	# print(str(parent1))
	# print(str(parent2))

	crossover = random.randint(0, len(parent1.sol))				#Determine the crossover point from where the genes will be exchanging between parents
	firstParent = random.randint(0, 2)							#Determine if parent1 or parent2 is the first part of the child (0 if parent1, 1 if parent2)
	child = Solution()

	if firstParent == 0:
		for i in range(0, crossover):
			child.sol.append(parent1.sol[i])
	else:
		for i in range(0, crossover):
			child.sol.append(parent2.sol[i])
		
	#Here we reached the crossover so we start exchanging genes
	y = j = crossover

	if firstParent == 0:
		while y < len(parent2.sol):
			while parent2.sol[j] in child.sol:
				j = (j+1)%len(parent2.sol)
			child.sol.append(parent2.sol[j])
			y = y + 1
	else:
		while y < len(parent1.sol):
			while parent1.sol[j] in child.sol:
				j = (j+1)%len(parent1.sol)
			child.sol.append(parent1.sol[j])
			y = y + 1

	#CAN IMPLEMENT MUTATION
	child.calculateCost(prob)

	return child
	
def generateChildPopulation(prob, pop):


	childPop = Population()

	for i in range(0,len(pop.elements)):
		child = generateChild(prob, pop)
		LocalSearch.globalLocalSearch(child, prob)

		while pop.exist(child) or childPop.exist(child):
			child = generateChild(prob, pop)
			LocalSearch.globalLocalSearch(child, prob)
		
		childPop.addElement(child)

	return childPop

def getNewGeneration(pop, childPop):
	size1 = len(pop) 
	size2 = len(childPop)
	maxSize = size1 if size1 < size2 else size2					#Normally size1 = size2 but just in case we take the smallest
	newGen = Population()
	i = j = count = 0
	while i < size1 and j < size2 and count < maxSize: 						#Merging the two lists taking best solutions 
		if pop[i].cost < childPop[j].cost: 
			newGen.addElement(pop[i]) 
			i += 1

		else: 
			newGen.addElement(childPop[j]) 
			j += 1
		count += 1
	return newGen