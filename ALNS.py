# Pedro Pinheiro de Siqueira
# ALNS para Roteamento de Drones

import math
import random
import pickle
import DrawPath

########## Heurísticas
def HeuShaw(sol, q):
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

def HeuRand(sol, q):
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

def HeuPiorPos(sol, q): # Pior Posição
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

def HeuGreedy(sol, vet):
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

def HeuRegret(sol, vet):
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

# Cálculos necessários para o funcionamento total
    
def DisTotal(sol):
    dis = []
    for i in range(len(sol)):
        if i == 0:
            #print("Fiz a distância entre o Inicial e o " + str(sol[i]))
            dis = dis + [(((x[sol[i]-1]-xini))**2 + ((y[sol[i]-1]-yini))**2)**(1/2)]
        else:
            #print("Fiz a distância entre o " + str(sol[i]) + " e o " + str(sol[i-1]))
            dis = dis + [(((x[sol[i]-1]-x[sol[i-1]-1]))**2 + ((y[sol[i]-1]-y[sol[i-1]-1]))**2)**(1/2)]
    dis = dis + [(((x[sol[i]-1]-xini))**2 + ((y[sol[i]-1]-yini))**2)**(1/2)]
    #print("Fiz a distância entre o Inicial e o " + str(sol[i]))
    #print("Vetor de Distâncias: " + str(dis))
    return dis

#Distance between two points
def Distance(point1, point2):

    dis = (((x[point1-1]-x[point2-1]))**2 + ((y[point1-1]-y[point2-1]))**2)**(1/2)

    return dis


def CustoDrone(w,q,beta,dis,sol,bat):
    aux = 0
    auxbat = q
    Cdrone = 0 # Custo para o drone
    Cbat = 1000*sum(bat)
    while aux < len(sol):
        if bat[aux] == 0:
            if auxbat > dis[aux] + beta + (((x[sol[aux]-1]-xini))**2 + ((y[sol[aux]-1]-yini))**2)**(1/2):
                auxbat = auxbat - dis[aux] - beta
                Cdrone = Cdrone + dis[aux] + beta 
                aux = aux + 1
            else:
                auxbat = q - beta - (((x[sol[aux]-1]-xini))**2 + ((y[sol[aux]-1]-yini))**2)**(1/2)
                Cdrone = Cdrone + beta + (((x[sol[aux]-1]-xini))**2 + ((y[sol[aux]-1]-yini))**2)**(1/2) + (((x[sol[aux-1]-1]-xini))**2 + ((y[sol[aux-1]-1]-yini))**2)**(1/2)
                aux = aux + 1
        else:
            if auxbat > dis[aux]:
                Cdrone = Cdrone + dis[aux] + beta + q - auxbat
                auxbat = q
                aux = aux + 1
            else:
                Cdrone = Cdrone + beta + (((x[sol[aux]-1]-xini))**2 + ((y[sol[aux]-1]-yini))**2)**(1/2) + (((x[sol[aux-1]-1]-xini))**2 + ((y[sol[aux-1]-1]-yini)**2))**(1/2)
                auxbat = q
                aux = aux + 1
    Cdrone = Cdrone + dis[len(dis)-1]
    CusTot = Cdrone + Cbat + w*1
    
    return CusTot

def CustoTotal(sol, bat):
    # Existem dois tipos de drones
    # O primeiro custa 1200, consegue andar 17664 metros de autonomia e 1920 para inspecionar o local 
    # O segundo custa 2000, consegue andar 19008 metros de autonomia e 1540 para inspecionar o local
    W1 = 1200 # Drone 1 -cost
    W2 = 2000 # Drone 2 -cost
    Q1 = 17664 #Battery autonomy 1
    Q2 = 19008 #Battery autonomy 2

    beta1 = 960*2; # 60 segundos x 3
    beta2 = 770*2; # 35 segundos x 3

    #Cbat = 1000*sum(bat)
    
    dis = DisTotal(sol)
    
    # Para o Primeiro Tipo de Drone
    CusTot1 = CustoDrone(W1,Q1,beta1,dis,sol,bat)

    # Para o Segundo Tipo de Drone
    CusTot2 = CustoDrone(W2,Q2,beta2,dis,sol,bat)

    #print("Custo total do Segundo tipo de Drone: " + str(CusTot2))
    if CusTot1 > CusTot2:
        drone = 2
    else:
        drone = 1

    return CusTot1, CusTot2, drone


###############################################################################
# Local Search

# Hill Climbing, 2-opt first-improvement local search
def LocalSearch2opt(sol):
    improve = True
    maxCount = 100
    count = 0
    while improve and count < maxCount:
        improve = False   
        for i in range(len(sol)-3) : #for each i in the hamiltonian path
            count = count + 1
            j = i + 2
            if count < maxCount :
                return sol
            if Distance(sol[i], sol[i+1]) + Distance(sol[j], sol[j+1]) > Distance(sol[i], sol[j]) + Distance(sol[i+1], sol[j+1]) :                   
                tmp = sol[i+1]
                sol[i+1] = sol[j]
                sol[j] = tmp
                improve = True

    return sol

# Hill Climbing, best-improvement local search
def LocalSearchBestImp(sol):
    improve = True
    maxCount = 100
    count = 0
    while improve and count < maxCount:
       
        bestImprove = 0
        besti = 0
        bestj = 2
        improve = False
        
        for i in range(len(sol)-3) : #for each i in the hamiltonian path
            count = count + 1
            j = i + 2
            
            if count < maxCount :
                return sol
            if Distance(sol[i], sol[i+1]) + Distance(sol[j], sol[j+1]) > Distance(sol[i], sol[j]) + Distance(sol[i+1], sol[j+1]) :                   
                
                improve = True                  #There is at least one improvement
                newImprove = Distance(sol[i], sol[i+1]) + Distance(sol[j], sol[j+1]) - Distance(sol[i], sol[j]) + Distance(sol[i+1], sol[j+1])
                
                if bestImprove < newImprove:    #if there is multiple improvements, we chose the best one
                    bestImprove = newImprove
                    besti = i
                    bestj = j
        
        if improve: #if there is an improvement, we change the solution to use it
            tmp = sol[besti+1]
            sol[besti+1] = sol[bestj]
            sol[bestj] = tmp

    return sol
   

# Swap, inter first-improvement local search
def LocalSearchSwap(sol):
    improve = True
    while improve :
        improve = False
        i = random.randint(1,len(sol)-2)

        for cpt in range(len(sol)-2) : #for each i in the hamiltonian path
            if cpt != i:

                distanceCour = Distance(sol[cpt-1], sol[cpt]) + Distance(sol[cpt], sol[cpt+1]) + Distance(sol[i-1], sol[i]) + Distance(sol[i], sol[i+1])
                newDistance = Distance(sol[cpt-1], sol[i]) + Distance(sol[i], sol[cpt+1]) + Distance(sol[i-1], sol[cpt]) + Distance(sol[cpt], sol[i+1])
                if distanceCour > newDistance :                   
                    tmp = sol[i]
                    sol[i] = sol[cpt]
                    sol[cpt] = tmp
                    improve = True

    return sol


def globalLocalSearch(sol):
    i = random.randint(0,2)
    newSol = sol
    for cpt in range(3):
        if i == 0:
            LocalSearch2opt(newSol)
        elif i == 1:
            LocalSearchBestImp(newSol)
        elif i == 2:
            LocalSearchSwap(newSol)
        i = (i+1) % 3
    return newSol

# setBatteries  @deprecated
#
# Description : find the best way to create batteries in nodes so that the drone can fly all the way
# and it costs less as possible, for the 1st model (Any node can be a battery)
#
#sol : the solution where we set the batteries
#distMax : the autonomy of a drone, distance it can fly without recharging
#
#return bat : vector of boolean, 1 if the node is a battery, 0 if it isn't
def setBatteries(sol, distMax):
    bat = []
    distCour = (((x[sol[0]-1]-xini))**2 + ((y[sol[0]-1]-yini))**2)**(1/2) #Dist between initial node and first node 
    
    if distCour > distMax:
        print("\n[ERROR] : Distance between initial point and node " + str(sol[0]) + " too long for the drone's autonomy.")
        return None
    for i in range(0, len(sol)-1):
        distCour = distCour + Distance(sol[i], sol[i+1])
        if distCour > distMax:
            if Distance(sol[i], sol[i+1]) > distMax:
                print("\n[ERROR] : Distance between node "+ str(sol[i]) + " and node " + str(sol[i+1]) + " too long for the drone's autonomy.")
                return None
            bat += [1]
            distCour = Distance(sol[i], sol[i+1])
        else:
            bat += [0]

    distLast = (((x[sol[len(sol)-1]-1]-xini))**2 + ((y[sol[len(sol)-1]-1]-yini))**2)**(1/2) #Dist between initial node and last node 
    
    distCour = distCour + distLast

    if distCour > distMax:
        if distLast > distMax:
            print("\n[ERROR] : Distance between node "+ str(sol[len(sol)-1]) + " and initial point too long for the drone's autonomy.")
            return
        bat += [1]
    else:
        bat += [0]

    return bat


# findBatteries
#
# Description : find the best way to join the critical path to batteries so that the drone can fly all the way
# and it costs less as possible, for the 2st model (Nodes to visit and batteries are different)
#
#sol : the solution where we set the batteries
#distMax : the autonomy of a drone, distance it can fly without recharging
#
#return bat : vector of batteries. 
# bat[i] = 0 if sol[i] can go to sol[i+1] without recharging.
# bat[i] = {x,y} if sol[i] needs to go to the battery's position {x,y} before going to sol[i+1]

def findBatteries(sol, distMax, batteries):
    bat = []
    distCour = (((x[sol[0]-1]-xini))**2 + ((y[sol[0]-1]-yini))**2)**(1/2) #Dist between initial node and first node 
    


###############################################################################
# Programa Principal
  
global x
global y
global xini
global yini
global _NB_ITE_MAX
global _AUTONOMY

_NB_ITE_MAX = 200
_AUTONOMY = 20000

#xini = 5
#yini = 5    
#x = [4, 3, 7, 2, 1, 9, 4, 6, 10, 11] # 4, 9, 2] 
#y = [5, 9, 1, 4, 4, 2, 9, 8, 8, 10] # 11, 8, 8] 

filename='ParaServidor_11_12/Ins100PerEInspire'

objects=[]
with (open(filename+'.pk1','rb')) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
            
Dados = objects[0]
xini = Dados.Onode[0][0]*1000
yini = Dados.Onode[0][1]*1000
#print(Dados.Onode)
#print(xini)
#print(yini)
x = []
y = []
for i in range(len(Dados.Cset)):
    x = x + [Dados.Cset[i][0]*1000]
    y = y + [Dados.Cset[i][1]*1000]

#print(x)
#print(Dados.Cset[0][1])
#print(len(y))
#print(Dados.Cset)
#print(len(Dados.Cset))


Solucao = [] # vetor solução
for i in range(len(x)):
    Solucao = Solucao + [i+1]

random.shuffle(Solucao)
# print("Solução Inicial: " + str(Solucao))


# vetor binário de baterias
# bat = []
# for i in range(len(Solucao)):
#     bat = bat + [round(random.random())]
# print("Baterias: " + str(bat))


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
    

#Solucao, vet = HeuShaw(Solucao, 3)
#print("Solução Atual: " + str(Solucao))
#print("Vetor Auxiliar: " + str(vet))
#Solucao = HeuRegret(Solucao,vet)
#print("Vetor Final: " + str(Solucao))

#Draw initial solution :

# DrawPath.subplot(1, 2, 1)
# DrawPath.setPlotTitle("Initial solution", fontsize=19)

# DrawPath.drawPoints(xini, yini, x, y)
# DrawPath.drawLines(xini, yini, x, y, Solucao)


# ALNS:

#C1, C2 = CustoTotal(sol)
D1 = sum(DisTotal(Solucao))
ite = 0;
BestVet = Solucao.copy()
#BestS = min(C1,C2)
BestD = D1
print("\nDistância Inicial: " + str(BestD))
print("Vetor Melhor Resultado Atual: " + str(BestVet))
q = round(len(x)/4)

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
        
    #print("Vetor Remoção: " + str(VetRemAux))
    #print("Vetor Inserção: " + str(VetInsAux))

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

    #print("Auxiliar Remoção: " + str(AuxRem))
    #print("Auxliar Inserção: " + str(AuxIns))
    #print("Melhor Solução Atualizada: " + str(BestVet))

    SolAux = Solucao.copy()
    #print("Solução Auxiliar: " + str(SolAux))

    # Removendo itens da solução
    if AuxRem == 0:
        SolAux, vet = HeuShaw(SolAux, q)
    elif AuxRem == 1:
        SolAux, vet = HeuRand(SolAux, q)
    elif AuxRem == 2:        
        SolAux, vet = HeuPiorPos(SolAux, q)

    # Inserindo itens da solução
    if AuxIns == 0:
        SolAux = HeuGreedy(SolAux, vet)
    elif AuxIns == 1:
        SolAux = HeuRegret(SolAux, vet)

    #print("Solução Auxiliar Atualizada: " + str(SolAux))

    #C1aux, C2aux = CustoTotal(SolAux)
    #CAux = min(C1aux,C2aux)
    #print("Melhor Solução da Iteração " + str(ite) + ": " + str(CAux) + "\n")
    Daux = sum(DisTotal(SolAux)) # Distância auxiliar
    #print("Melhor Solução da Iteração " + str(ite) + ": " + str(Daux) + "\n")

    #print("\n Iteração: " + str(ite))
    #print("Melhor resultado até agora: " + str(BestD))
    #print("Resultado gerado agora: " + str(Daux))
    #print("Solução Auxiliar Atual: " + str(SolAux))
    #print("Melhor Solução Atualizada: " + str(BestVet))
    # Comparando a nova solução com a melhor solução que existe

    # print("BEFORE SEARCH")
    # print("Best sol : ", str(SolAux), " = ", str(Daux))
    LocalSol = globalLocalSearch(SolAux)
    LocalDis = sum(DisTotal(LocalSol))

    # print("")
    # print("AFTER SEARCH")
    # print("Best sol : ", str(LocalSol), " = ", str(LocalDis))
    # print("\n")

    if BestD > LocalDis:
        # print("\n\nIteração: " + str(ite))
        # print("Resultado novo: " + str(LocalDis))
        BestD = LocalDis
        # print("Solução Auxiliar Atual: " + str(LocalSol))
        BestVet = LocalSol.copy()
        # print("Melhor Solução Atualizada: " + str(BestVet))
        Solucao = LocalSol.copy()

       

        #print("Solução Atualizada: " + str(Solucao))
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

bat = setBatteries(BestVet, _AUTONOMY)

print("\nEsta foi a melhor distância final encontrada: " + str(BestD))
#print("Solução Auxiliar Final: " + str(SolAux))
#print("Solução Final: " + str(Solucao))
print("Melhor Solução Final: " + str(BestVet))

# DrawPath.subplot(1, 2, 2)   #For 2 figures

DrawPath.subplot(1, 1, 1)
DrawPath.setPlotTitle("Best solution found", fontsize=19)

if bat == None:
    DrawPath.drawPoints(xini, yini, x, y)
else:
    DrawPath.drawPoints(xini, yini, x, y, bat)

DrawPath.drawLines(xini, yini, x, y, BestVet)
DrawPath.draw()


#print("E estas são as distâncias deste vetor: " + str(DisTotal(BestVet)))
#print("Soma: " + str(sum(DisTotal(BestVet))))
#print("Distância Auxiliar Final: " + str(Daux))
#print("Os vetores de pesos ficaram:")
#print("Vetor Remoção: " + str(VetRemAux))
#print("Vetor Inserção: " + str(VetInsAux))
#dis = []
#for i in range(len(sol)):
#    if i == 0:
#        dis = dis + [((x[sol[i]-1]-xini)**2 + (y[sol[i]-1]-yini)**2)*50]
#    else:
#        dis = dis + [((x[sol[i]-1]-x[sol[i-1]-1])**2 + (y[sol[i]-1]-y[sol[i-1]-1])**2)*50]
#print("Distância = " + str(dis))
#print("Baterias: " + str(bat))
'''
VetBat = [1, 1]
VetBatAux = [0, 0]

ite = 0
C1, C2, drone = CustoTotal(BestVet, bat)
BestC = min(C1,C2)
print("\nMelhor Custo Inicial: " + str(BestC))
#print("Vetor Inicial das baterias: " + str(bat))


while ite < 100:
    # Calculando valores dos vetores de Remoção e Inserção
    for i in range(len(VetBat)):
        VetBatAux[i] = VetBat[i]/sum(VetBat)
        if i > 0:
            VetBatAux[i] = VetBatAux[i] + VetBatAux[i-1]
            
    # Vendo qual heurística será utilizada
    AuxBat = random.random()
    for i in range(len(VetBatAux)):
        if AuxBat <= VetBatAux[i]:
            AuxBat = i
            break
    
    SolAux = bat
    
    if AuxBat == 0:
        SolAux = BitSwap(SolAux)
    elif AuxBat == 1:
        SolAux = BitChange(SolAux)
    
    C1aux, C2aux, droneaux = CustoTotal(BestVet, SolAux)
    CAux = min(C1aux,C2aux)
    #print("Melhor Custo da Iteração " + str(ite) + ": " + str(CAux) + "\n")
    
    if BestC > CAux:
        BestC = CAux
        BestVetBat = SolAux
        bat = SolAux
        drone = droneaux
        VetBat[AuxBat] = VetBat[AuxBat]*1.25 #+ 0.5
    else:
        VetBat[AuxBat] = VetBat[AuxBat]*0.75 #- 0.5
    
    ite = ite + 1

print("Este foi o melhor custo encontrado: " + str(BestC))
print("Este é o vetor utilizado para isso: " + str(BestVetBat))
print("Para tal é utilizado o " + str(drone) + "º drone")'''