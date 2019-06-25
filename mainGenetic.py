import DrawPath
import math
import random
import Utils
import Genetic
import Batteries
import LocalSearch
import time
from Classes.problem import Problem
from Classes.population import Population
from Classes.solution import Solution

global _NB_ITE_MAX
global _AUTONOMY

_NB_ITE_MAX = 500
_AUTONOMY = 20000


filename='ParaServidor_11_12/Ins20PerEPhantom'

prob = Problem(filename)
pop = Genetic.generateRandomPopulation(prob, 50)

print(pop)

for i in range(0, _NB_ITE_MAX):
	if i%500 == 0:
		Genetic.mixWithRandomSolutions(prob, pop)
	childPop = Genetic.generateChildPopulation(prob, pop)
	pop = Genetic.getNewGeneration(pop, childPop)

print(pop)
