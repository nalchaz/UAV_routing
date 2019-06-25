# @author : Nahel Chazot
# Local search methods for TSP problem

import random
import Utils
from Classes.solution import Solution
from Utils import timing

# Hill Climbing, 2-opt first-improvement local search
def LocalSearch2opt(sol, prob):
    improve = True
    maxCount = 10000
    count = 0
    while improve and count < maxCount:
        improve = False   
        for i in range(len(sol.sol)-3) : #for each i in the hamiltonian path
            count = count + 1
            j = i + 2
            if count > maxCount :
                
                return sol.sol
            if Utils.Distance(sol.sol[i], sol.sol[i+1], prob) + Utils.Distance(sol.sol[j], sol.sol[j+1], prob) > Utils.Distance(sol.sol[i], sol.sol[j], prob) + Utils.Distance(sol.sol[i+1], sol.sol[j+1], prob) :                   
                tmp = sol.sol[i+1]
                sol.sol[i+1] = sol.sol[j]
                sol.sol[j] = tmp
                improve = True
    
    return sol

# Hill Climbing, best-improvement local search
def LocalSearchBestImp(sol, prob):
    improve = True
    maxCount = 10000
    count = 0
    while improve and count < maxCount:
       
        bestImprove = 0
        besti = 0
        bestj = 2
        improve = False
        
        for i in range(len(sol.sol)-3) : #for each i in the hamiltonian path
            count = count + 1
            j = i + 2
            
            if count > maxCount :
                
                return sol.sol
            if Utils.Distance(sol.sol[i], sol.sol[i+1], prob) + Utils.Distance(sol.sol[j], sol.sol[j+1], prob) > Utils.Distance(sol.sol[i], sol.sol[j], prob) + Utils.Distance(sol.sol[i+1], sol.sol[j+1], prob) :                   
                
                improve = True                  #There is at least one improvement
                newImprove = Utils.Distance(sol.sol[i], sol.sol[i+1], prob) + Utils.Distance(sol.sol[j], sol.sol[j+1], prob) - Utils.Distance(sol.sol[i], sol.sol[j], prob) + Utils.Distance(sol.sol[i+1], sol.sol[j+1], prob)
                
                if bestImprove < newImprove:    #if there is multiple improvements, we chose the best one
                    bestImprove = newImprove
                    besti = i
                    bestj = j
        
        if improve: #if there is an improvement, we change the solution to use it
            tmp = sol.sol[besti+1]
            sol.sol[besti+1] = sol.sol[bestj]
            sol.sol[bestj] = tmp
    
    return sol.sol
   

# Swap, inter first-improvement local search
def LocalSearchSwap(sol, prob):
    improve = True
    while improve :
        improve = False
        i = random.randint(1,len(sol)-2)

        for cpt in range(len(sol)-2) : #for each i in the hamiltonian path
            if cpt != i:

                distanceCour = Utils.Distance(sol[cpt-1], sol[cpt], prob) + Utils.Distance(sol[cpt], sol[cpt+1], prob) + Utils.Distance(sol[i-1], sol[i], prob) + Utils.Distance(sol[i], sol[i+1], prob)
                newDistance = Utils.Distance(sol[cpt-1], sol[i], prob) + Utils.Distance(sol[i], sol[cpt+1], prob) + Utils.Distance(sol[i-1], sol[cpt], prob) + Utils.Distance(sol[cpt], sol[i+1], prob)
                if distanceCour > newDistance :                   
                    tmp = sol[i]
                    sol[i] = sol[cpt]
                    sol[cpt] = tmp
                    improve = True

    return sol

#Use each local search one after an other, starting by a random one
def globalLocalSearch(sol, prob):
    i = random.randint(0,2)
    newSol = sol.copy()
    for cpt in range(3):
        if i == 0:
            LocalSearch2opt(newSol, prob)
        elif i == 1:
            LocalSearchBestImp(newSol, prob)
        # elif i == 2:
        #     LocalSearchSwap(newSol, prob)
        i = (i+1) % 3
    return newSol