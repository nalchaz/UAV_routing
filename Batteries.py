import Utils
from Utils import timing

# setBatteries  @deprecated
#
# Description : find the best way to create batteries in nodes so that the drone can fly all the way
# and it costs less as possible, for the 1st model (Any node can be a battery)
#
#sol : the solution where we set the batteries
#distMax : the autonomy of a drone, distance it can fly without recharging
#
#return bat : vector of boolean, 1 if the node is a battery, 0 if it isn't
def setBatteries(sol, distMax, prob):

    x = prob.x
    y = prob.y
    xini = prob.xini
    yini = prob.yini

    bat = []
    distCour = (((x[sol[0]-1]-xini))**2 + ((y[sol[0]-1]-yini))**2)**(1/2) #Dist between initial node and first node 
    
    if distCour > distMax:
        print("\n[ERROR] : Distance between initial point and node " + str(sol[0]) + " too long for the drone's autonomy.")
        return None
    for i in range(0, len(sol)-1):
        distCour = distCour + Utils.Distance(sol[i], sol[i+1], prob)
        if distCour > distMax:
            if Utils.Distance(sol[i], sol[i+1], prob) > distMax:
                print("\n[ERROR] : Distance between node "+ str(sol[i]) + " and node " + str(sol[i+1]) + " too long for the drone's autonomy.")
                return None
            bat += [1]
            distCour = Utils.Distance(sol[i], sol[i+1], prob)
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