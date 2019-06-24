import DrawPath
import math
import random
import Utils
import ALNS
import Batteries
import LocalSearch
import time
from Classes.problem import Problem

global _NB_ITE_MAX
global _AUTONOMY

_NB_ITE_MAX = 2
_AUTONOMY = 20000

#xini = 5
#yini = 5    
#x = [4, 3, 7, 2, 1, 9, 4, 6, 10, 11] # 4, 9, 2] 
#y = [5, 9, 1, 4, 4, 2, 9, 8, 8, 10] # 11, 8, 8] 

filename='ParaServidor_11_12/Ins100PerEPhantom'

prob = Problem(filename)

Solucao = [] # vetor solução
for i in range(len(prob.x)):
    Solucao = Solucao + [i+1]

random.shuffle(Solucao)

startTotalTime = time.time()
heuGreedyTime = 0
heuRegretTime = 0
heuShawTime = 0
heuRandTime = 0
heuPiorPosTime = 0
localSearchTime = 0

VetRem = [1, 1, 1];
VetIns = [1, 1];

VetRemAux = [0, 0, 0];
for i in range(len(VetRem)):
    VetRemAux[i] = VetRem[i]/sum(VetRem)
    if i > 0:
        VetRemAux[i] = VetRemAux[i] + VetRemAux[i-1]
        
VetInsAux = [0, 0];
for i in range(len(VetIns)):
    VetInsAux[i] = VetIns[i]/sum(VetIns)
    if i > 0:
        VetInsAux[i] = VetInsAux[i] + VetInsAux[i-1]
    

#Draw initial solution :

# DrawPath.subplot(1, 2, 1)
# DrawPath.setPlotTitle("Initial solution", fontsize=19)

# DrawPath.drawPoints(xini, yini, x, y)
# DrawPath.drawLines(xini, yini, x, y, Solucao)


# ALNS:

#C1, C2 = CustoTotal(sol)
D1 = Utils.DisTotal(Solucao, prob)
ite = 0;
BestVet = Solucao.copy()
#BestS = min(C1,C2)
BestD = D1
print("\nDistância Inicial: " + str(BestD))
q = round(len(prob.x)/4)

# Escolhendo o primeiro valor que será utilizado na LNS

while ite < _NB_ITE_MAX:
    # Calculando valores dos vetores de Remoção e Inserção
    for i in range(len(VetRem)):
        VetRemAux[i] = VetRem[i]/sum(VetRem)
        if i > 0:
            VetRemAux[i] = VetRemAux[i] + VetRemAux[i-1]
    
    for i in range(len(VetIns)):
        VetInsAux[i] = VetIns[i]/sum(VetIns)
        if i > 0:
            VetInsAux[i] = VetInsAux[i] + VetInsAux[i-1]

    # Vendo qual heurística será utilizada
    AuxRem = random.random()
    for i in range(len(VetRemAux)):
        if AuxRem <= VetRemAux[i]:
            AuxRem = i
            break

    AuxIns = random.random()
    for i in range(len(VetInsAux)):
        if AuxIns <= VetInsAux[i]:
            AuxIns = i
            break


    SolAux = Solucao.copy()

    # Removendo itens da solução
    if AuxRem == 0:
        start = time.time()
        SolAux, vet = ALNS.HeuShaw(SolAux, q, prob)
        heuShawTime = heuShawTime + time.time() - start
    elif AuxRem == 1:
        start = time.time()
        SolAux, vet = ALNS.HeuRand(SolAux, q, prob)
        heuRandTime = heuRandTime + time.time() - start
    elif AuxRem == 2:  
        start = time.time()      
        SolAux, vet = ALNS.HeuPiorPos(SolAux, q, prob)
        heuPiorPosTime = heuPiorPosTime + time.time() - start

    # Inserindo itens da solução
    if AuxIns == 0:
        start = time.time()
        SolAux = ALNS.HeuGreedy(SolAux, vet, prob)
        heuGreedyTime = heuGreedyTime + time.time() - start
    elif AuxIns == 1:
        start = time.time()
        SolAux = ALNS.HeuRegret(SolAux, vet, prob)
        heuRegretTime = heuRegretTime + time.time() - start

    Daux = Utils.DisTotal(SolAux, prob)

    # LOCAL SEARCH
    start = time.time()
    LocalSol = LocalSearch.globalLocalSearch(SolAux, prob)
    localSearchTime = localSearchTime + time.time() - start
    LocalDis = Utils.DisTotal(LocalSol, prob)


    if BestD > LocalDis:

        BestD = LocalDis
        BestVet = LocalSol.copy()
        Solucao = LocalSol.copy()

        VetRem[AuxRem] = VetRem[AuxRem]*1.25 #+ 0.5
        VetIns[AuxIns] = VetIns[AuxIns]*1.25 #+ 0.5
    else:
        VetRem[AuxRem] = VetRem[AuxRem]*0.75 #- 0.5
        VetIns[AuxIns] = VetIns[AuxIns]*0.75 #- 0.5
        #if VetRem[AuxRem] == 0:
        #    VetRem[AuxRem] = 0.5;
        #if VetIns[AuxIns] == 0:
        #    VetIns[AuxIns] = 0.5;
            
    ite = ite + 1

bat = Batteries.setBatteries(BestVet, _AUTONOMY, prob)


totalTime = time.time() - startTotalTime

print('HeuRand function took {:.3f} ms'.format(heuRandTime*1000.0))
print('HeuShaw function took {:.3f} ms'.format(heuShawTime*1000.0))
print('HeuPiorPos function took {:.3f} ms'.format(heuPiorPosTime*1000.0))
print('HeuGreedy function took {:.3f} ms'.format(heuGreedyTime*1000.0))
print('HeuRegret function took {:.3f} ms'.format(heuRegretTime*1000.0))
print('LocalSearch function took {:.3f} ms'.format(localSearchTime*1000.0))
print('Global program took {:.3f} s'.format(totalTime))

print("\nEsta foi a melhor distância final encontrada: " + str(BestD))

# print("Melhor Solução Final: " + str(BestVet))

# DrawPath.subplot(1, 2, 2)   #For 2 figures

DrawPath.subplot(1, 1, 1)
DrawPath.setPlotTitle("Best solution found", fontsize=19)

if bat == None:
    DrawPath.drawPoints(prob.xini, prob.yini, prob.x, prob.y)
else:
    DrawPath.drawPoints(prob.xini, prob.yini, prob.x, prob.y, bat)

DrawPath.drawLines(prob.xini, prob.yini, prob.x, prob.y, BestVet)
DrawPath.draw()