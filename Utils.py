import time

#Gives the duration of a function
# To use it :
# simply put '@timing' before the definition of a function
#
# example :
#
#   @timing
#   def HeuGreedy()
#       code
#   
#Traceback : HeuGreedy function took 8.998 ms
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap

def DisTotal(sol, prob):
    dis = 0
    for i in range(len(sol)):
        if i == 0:
            dis += prob.distanceIni[sol[i]]
        else:
            dis += prob.distances[sol[i]][sol[i-1]]
    dis += prob.distanceIni[sol[len(sol)-1]]

    return dis

#Distance between two points
def Distance(point1, point2, prob):

    return prob.distances[point1][point2]


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
