# Pedro Pinheiro de Siqueira
# ALNS para Roteamento de Drones

import math
import random
from Utils import timing

########## Heurísticas
def HeuShaw(sol, q, prob):

    x = prob.x
    y = prob.y
    xini = prob.xini
    yini = prob.yini

    #print('Heurística Shaw')    
    vet = []
    aux = random.randint(0,len(sol)-1)
    dis = []
    vet.append(sol[aux])
    del(sol[aux])
    for i in range(0,len(sol)):
        dis.append((x[vet[0]-1]-x[sol[i]-1])**2+(y[vet[0]-1]-y[sol[i]-1])**2)
    
    while len(vet) < q:
        #print("Solução Atual: " + str(sol))
        #print("Distância Atual: " + str(dis))
        vet.append(sol[dis.index(min(dis))])
        del(sol[dis.index(min(dis))])
        del(dis[dis.index(min(dis))])
    return sol,vet

def HeuRand(sol, q, prob):

    x = prob.x
    y = prob.y
    xini = prob.xini
    yini = prob.yini

    #print('Heurística Randômica')
    vet = []
    while q > 0:
        aux = random.randint(0,len(sol)-1)
        #print("Auxiliar randomizado: " + str(aux))
        vet.append(sol[aux])
        del(sol[aux])
        q = q - 1
        #print("Solução Agora: " + str(sol))
        #print("Vetor Auxiliar novo: " + str(vet))
    return sol, vet

def HeuPiorPos(sol, q, prob): # Pior Posição

    x = prob.x
    y = prob.y
    xini = prob.xini
    yini = prob.yini

    #print('Heurística Da Pior Posição')
    vet = []
    while len(vet) < q:
        #dis = []
        #for i in range(len(sol)):
        #    if i == 0:
        #        dis = dis + [((x[sol[i]-1]-xini)**2 + (y[sol[i]-1]-yini)**2)*50]
        #    else:
        #        dis = dis + [((x[sol[i]-1]-x[sol[i-1]-1])**2 + (y[sol[i]-1]-y[sol[i-1]-1])**2)*50]
        #print("Distâncias: " + str(dis))
        DisTot = []
        for i in range(len(sol)):
            DisTot.append(0)
            if i == 0:
                DisTot[i] = ((x[sol[i]-1]-xini)**2 + (y[sol[i]-1]-yini)**2)*50 + ((x[sol[i]-1]-x[sol[i+1]-1])**2 + (y[sol[i]-1]-y[sol[i+1]-1])**2)*50
            elif i == len(sol)-1:
                DisTot[i] = ((x[sol[i]-1]-xini)**2 + (y[sol[i]-1]-yini)**2)*50 + ((x[sol[i]-1]-x[sol[i-1]-1])**2 + (y[sol[i]-1]-y[sol[i-1]-1])**2)*50
            else:
                DisTot[i] = ((x[sol[i]-1]-x[sol[i-1]-1])**2 + (y[sol[i]-1]-y[sol[i-1]-1])**2)*50 + ((x[sol[i]-1]-x[sol[i+1]-1])**2 + (y[sol[i]-1]-y[sol[i+1]-1])**2)*50

        #print("Distâncias Totais: " + str(DisTot))
        aux = DisTot.index(max(DisTot))
        #print(aux)
        vet.append(sol[aux])
        del(sol[aux])
        #print("Nova Solução: " + str(sol))
        #print("Vetor Auxiliar novo: " + str(vet))
    return sol, vet

def HeuGreedy(sol, vet, prob):

    x = prob.x
    y = prob.y
    xini = prob.xini
    yini = prob.yini

    #print('Heurística Gulosa')
    while vet != []:
        MenorGanho = math.inf
        MelhorPosicao = 0
        MelhorIndice = 0
        for i in range(len(vet)):
            for j in range(len(sol)+1):
                if j == 0:                 
                    aux = (x[vet[i]-1]-xini)**2 + (y[vet[i]-1]-yini)**2
                    aux = aux + (x[vet[i]-1]-x[sol[j]-1])**2 + (y[vet[i]-1]-y[sol[j]-1])**2
                elif j == len(sol):
                    aux = (x[vet[i]-1]-xini)**2 + (y[vet[i]-1]-yini)**2
                    aux = aux + (x[vet[i]-1]-x[sol[j-1]-1])**2 + (y[vet[i]-1]-y[sol[j-1]-1])**2
                else:
                    aux = (x[vet[i]-1]-x[sol[j-1]-1])**2 + (y[vet[i]-1]-y[sol[j-1]-1])**2
                    aux = aux + (x[vet[i]-1]-x[sol[j]-1])**2 + (y[vet[i]-1]-y[sol[j]-1])**2
                if aux < MenorGanho:
                    #print("Auxiliar: " + str(aux))
                    #print("Melhor Posição: " + str(j))
                    #print("Melhor índice: " + str(vet[i]))
                    MenorGanho = aux
                    MelhorPosicao = j
                    MelhorIndice = i
        #print("Solução Atual: " + str(sol))
        #print("Vetor a ser adicionado: " + str(vet))
        #print("Melhor Posição: " + str(MelhorPosicao))
        #print("Melhor índice: " + str(vet[MelhorIndice]))
        sol.insert(MelhorPosicao,vet[MelhorIndice])
        del(vet[MelhorIndice])
        #print("Solução Agora: " + str(sol))
        #print("Vetor Agora: " + str(vet))
    return sol

def HeuRegret(sol, vet, prob):

    x = prob.x
    y = prob.y
    xini = prob.xini
    yini = prob.yini

    #print('Heurística do Arrependimento')
    while vet != []:
        MelhorPosicao = []
        Ganhos = []
        for i in range(len(vet)):
            MenorGanho = math.inf
            MaiorGanho = 0
            MelhorPosicao.append(0)
            for j in range(len(sol)+1):
                if j == 0:                 
                    aux = (x[vet[i]-1]-xini)**2 + (y[vet[i]-1]-yini)**2
                    aux = aux + (x[vet[i]-1]-x[sol[j]-1])**2 + (y[vet[i]-1]-y[sol[j]-1])**2
                elif j == len(sol):
                    aux = (x[vet[i]-1]-xini)**2 + (y[vet[i]-1]-yini)**2
                    aux = aux + (x[vet[i]-1]-x[sol[j-1]-1])**2 + (y[vet[i]-1]-y[sol[j-1]-1])**2
                else:
                    aux = (x[vet[i]-1]-x[sol[j-1]-1])**2 + (y[vet[i]-1]-y[sol[j-1]-1])**2
                    aux = aux + (x[vet[i]-1]-x[sol[j]-1])**2 + (y[vet[i]-1]-y[sol[j]-1])**2
                if aux < MenorGanho:
                    MenorGanho = aux
                    MelhorPosicao[i] = j
                if aux > MaiorGanho:
                    MaiorGanho = aux
            Ganhos.append(MaiorGanho-MenorGanho)
        #print("Solução Atual: " + str(sol))
        #print("Vetor a ser adicionado: " + str(vet))
        #print("Ganhos: " + str(Ganhos))
        #print("Melhores Posições: " + str(MelhorPosicao))
        sol.insert(MelhorPosicao[Ganhos.index(max(Ganhos))],vet[Ganhos.index(max(Ganhos))])
        del(vet[Ganhos.index(max(Ganhos))])
        #print("Solução Nova: " + str(sol))
    return sol

def BitSwap(sol):
    aux = random.randint(0,len(sol)-1)
    aux2 = random.randint(0,len(sol)-1)
    while aux == aux2:
        aux2 = random.randint(0,len(sol)-1)
    #print("Solução Inicial: " + str(sol))
    #print("Auxiliar 1: " + str(aux))
    #print("Auxiliar 2: " + str(aux2))
    aux3 = sol[aux]
    sol[aux] = sol[aux2]
    sol[aux2] = aux3
    #print("Solução Final: " + str(sol))
    return sol    

def BitChange(sol):
    #print("Solução Inicial: " + str(sol))
    aux = random.randint(0,len(sol)-1)
    #print("Auxiliar: " + str(aux))
    if sol[aux] == 1:
        sol[aux] = 0
    else:
        sol[aux] = 1
    #print("Solução Final: " + str(sol))
    return sol 
