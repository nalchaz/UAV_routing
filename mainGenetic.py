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

_NB_ITE_MAX = 2
_AUTONOMY = 20000


filename='ParaServidor_11_12/Ins10PerEPhantom'

prob = Problem(filename)
pop = Genetic.generateRandomPopulation(prob, 50)

# print(str(pop))

# child = Genetic.generateChild(prob, pop)

# print(str(child))

childPop = Genetic.newGeneration(prob, pop)
print(pop)
print(childPop)