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

_POPULATION_SIZE = 100
_NB_ITE_MAX = 200
_AUTONOMY = 20000

filename='ParaServidor_11_12/Ins100PerEPhantom'

def displayBestSolutions(pop, prob):
	DrawPath.subplot(2, 2, 1)
	DrawPath.setPlotTitle("Solution 1", fontsize=19)

	bat = Batteries.setBatteries(pop.elements[0].sol, _AUTONOMY, prob)

	DrawPath.drawPoints(prob.xini, prob.yini, prob.x, prob.y, bat)
	DrawPath.drawLines(prob.xini, prob.yini, prob.x, prob.y, pop.elements[0].sol)

	DrawPath.subplot(2, 2, 2)
	DrawPath.setPlotTitle("Solution 2", fontsize=19)

	bat = Batteries.setBatteries(pop.elements[1].sol, _AUTONOMY, prob)

	DrawPath.drawPoints(prob.xini, prob.yini, prob.x, prob.y, bat)
	DrawPath.drawLines(prob.xini, prob.yini, prob.x, prob.y, pop.elements[1].sol)

	DrawPath.subplot(2, 2, 3)
	DrawPath.setPlotTitle("Solution 3", fontsize=19)

	bat = Batteries.setBatteries(pop.elements[2].sol, _AUTONOMY, prob)

	DrawPath.drawPoints(prob.xini, prob.yini, prob.x, prob.y, bat)
	DrawPath.drawLines(prob.xini, prob.yini, prob.x, prob.y, pop.elements[2].sol)

	DrawPath.subplot(2, 2, 4)
	DrawPath.setPlotTitle("Solution 4", fontsize=19)

	bat = Batteries.setBatteries(pop.elements[3].sol, _AUTONOMY, prob)

	DrawPath.drawPoints(prob.xini, prob.yini, prob.x, prob.y, bat)
	DrawPath.drawLines(prob.xini, prob.yini, prob.x, prob.y, pop.elements[3].sol)

	DrawPath.draw()



startTotalTime = time.time()

prob = Problem(filename)
pop = Genetic.generateRandomPopulation(prob, _POPULATION_SIZE)

print(pop)

for i in range(_NB_ITE_MAX):
	# child = Genetic.generateChild(prob, pop)
	# print(str(child))
	# print("")
	if i%15 == 0:
		Genetic.mixWithRandomSolutions(prob, pop)
	childPop = Genetic.generateChildPopulation(prob, pop)
	pop = Genetic.getNewGeneration(pop, childPop)

totalTime = time.time() - startTotalTime

print(pop)

print('Genetic algorithm took {:.3f} ms'.format(totalTime*1000.0))

displayBestSolutions(pop, prob)
