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


sol1 = Solution()
sol1.sol = [1,2,3,4,5,6]

sol2 = Solution()
sol2.sol = [1,2,3,4,5,6]

pop.addElement(sol1)
pop.addElement(sol2)

print(str(pop))