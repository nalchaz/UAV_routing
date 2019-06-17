# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:50:55 2018

@author: Roberto G. Ribeiro
"""# -*- coding: utf-8 -*-


import numpy as np
import math
from gurobipy import *
import itertools as it
import re

import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

from PatioNorte import PatioNorte 
from PatiosNorteSul import PatiosNorteSul
from ConverterFunctions import ConverterFunctions
from matplotlib.figure import Figure
import matplotlib.image as mpimg
import pylab as Pylab
import matplotlib.patches as mpatch



class VANTProblem(object):
    
    def __init__(self,Cset,Gset,Onode,W,Q,f,beta):
        self.Cset=Cset # Set of inspection nodes
        self.Gset=Gset # Set of supply nodes
        self.Onode=Onode # Start node
        self.W=W #Drone Cost
        self.Q=Q # Battery Autonomy
        self.f=f # vector of supply station cost
        self.beta=beta
        
    def method(self):
        return 'instance method called', self


    def ComputeVset(self):
        Vset=self.Onode
        Vset=np.concatenate((Vset,self.Cset))
        Vset=np.concatenate((Vset,self.Gset))
        return Vset

    def EuclidianDis(self,node1,node2):
        xdis=node2[0]-node1[0]
        ydis=node2[1]-node1[1]
        return math.sqrt(xdis**2 + ydis**2)

    def ComputeDisij(self,Vset):
        vsize=len(Vset)        
        dij=np.zeros((vsize,vsize))
        for i in range (0,vsize-1):
            for j in range (i+1,vsize):
                dis=self.EuclidianDis(Vset[i],Vset[j])*1000 # Km to m
                #dgh.append(dis)
                dij[i,j]=dis
                dij[j,i]=dis
        return dij
    
    def BuildModel(self,lpfilename):
        
        
        Vset=self.ComputeVset()
        dij=self.ComputeDisij(Vset)
        print('Distancias')
        print(dij)
        
        model=Model("VANT")
        
        xmat=[(i,j) for i in range(len(Vset)) for j in range(1,len(Vset)) if i!=j]
        x=model.addVars(xmat,vtype=GRB.BINARY,name='x')
        
        yvet=[(j) for j in range(len(self.Gset))]
        y=model.addVars(yvet,vtype=GRB.BINARY,name='y') 

        zvet=[(j) for j in range(len(self.Cset))]
        z=model.addVars(zvet,vtype=GRB.BINARY,name='z')   
        
        wvet=[(j) for j in range(len(self.Gset))]
        w=model.addVars(wvet,vtype=GRB.INTEGER,lb=0.0,ub=len(Vset),name='w')  
        
        pvet=[(j) for j in range(len(Vset))]
        p=model.addVars(pvet,lb=0.0,ub=self.Q,name='p') 
        
        tvet=[(j) for j in range(len(Vset))]
        t=model.addVars(tvet,lb=0.0,ub=len(Vset),name='t')         
        
        
        model.update()
        print('-------########################-')
        print(model.getVars())    
        
        """ Objective Function """
        
        expr1=quicksum(dij[i,j]*x[i,j] for i in range(len(Vset))
        for j in range(1,len(Vset)) if i!=j)
        
        expr2=quicksum((self.W+dij[0,j+1])*z[j] for j in range(len(self.Cset)))
        
        expr3=quicksum((self.W+dij[0,1+j+len(self.Cset)])*w[j] for j in range(len(self.Gset)))
        
        expr4=quicksum(self.f[j]*y[j] for j in range(len(self.Gset)))       
        obj=LinExpr(expr1+expr2+expr3+expr4)
        
        model.setObjective(obj,GRB.MINIMIZE)

        """ Constraints """
        
        #(2)
        
        for j in range(len(self.Cset)):
            expr2=quicksum(x[i,1+j] for i in range(len(Vset)) if i!=(j+1))
            model.addConstr(expr2 == 1,name="R2_"+str(1+j))
            
         
        #(2a)
        
        for j in range(len(self.Cset)):
            expr2a=quicksum(x[1+j,i] for i in range(1,len(Vset)) if i!=(j+1))
            model.addConstr(expr2a <= 1,name="R2a_"+str(1+j))            
            

        #(3)
            
        for j in range(1,len(self.Cset)+1):
            expr3a=quicksum(x[j,k] for k in range(1,len(Vset)) if j!=k)
            model.addConstr(expr3a==1-z[j-1],name="R3_"+str(j))
            
        #(4)
        
        for j in range(len(self.Gset)):
            expr4a=quicksum(x[1+j+len(self.Cset),k] for k in range(1,len(Vset)) if
                              (1+j+len(self.Cset)) != k)
            expr4b=quicksum(x[i,1+j+len(self.Cset)] for i in range(len(Vset)) if 
                              (1+j+len(self.Cset)) != i)
            model.addConstr(expr4a + w[j]==expr4b,name="R4_"+str(j))            

        #(5)
        
        expr5a=quicksum(x[0,j] for j in range(1,len(Vset)))
        expr5b=quicksum(z[j] for j in range(len(self.Cset)))
        expr5c=quicksum(w[j] for j in range(len(self.Gset)))
        model.addConstr(expr5a==expr5b+expr5c,name="R5")
        
        """
        #(5)
        for i in range(len(Vset)):
            for j in range(len(Vset)):
                if (i!=j):
                    model.addConstr(x[i,j]+x[j,i]<=1,name="R5_("+str(i)+","+
                                    str(j)+")")
        """

        #(6)
                    
        for j in range(len(self.Gset)):
            for i in range(len(Vset)):
                if (1+len(self.Cset)+j!=i):
                    model.addConstr(x[i,1+len(self.Cset)+j]<=y[j],name="R6a_("+
                                  str(i)+","+str(j)+")")
                    
        for j in range(len(self.Gset)):
            for i in range(1,len(Vset)):
                if (1+len(self.Cset)+j!=i):
                    model.addConstr(x[1+len(self.Cset)+j,i]<=y[j],name="R6b_("+
                                  str(j)+","+str(i)+")")                    
            
        #(7)

        expr7a=quicksum(x[i,j] for i in range(len(Vset)) for j
                       in range(1,len(Vset)) if i!=j)
        
        expr7b=quicksum(x[i,1+len(self.Cset)+j] for i in range(len(Vset))        
        for j in range(len(self.Gset))  if i!=(1+len(self.Cset)+j) )
        model.addConstr(expr7a == len(self.Cset) + expr7b,name="R7")                    

            
        #(8)
        model.addConstr(p[0]==self.Q,name="R8_("+str(0)+")" )
        for j in range(len(self.Cset)):
            for i in range(len(Vset)):
                if (i!=(1+j)):
                    model.addConstr(p[1+j] <= p[i] - (dij[i,1+j]+self.beta)*x[i,1+j] +
                                    (1-x[i,1+j])*self.Q,
                                    name="R8_("+str(i)+","+str(j+1)+")")   
                                       
             
        #(9)
        for j in range(len(self.Gset)):
            model.addConstr(p[1+j+len(self.Cset)]==self.Q*y[j],name="R9_"+str(j)) 


        #(10)  
        for i in range(1,len(self.Cset)+1):
            model.addConstr(p[i]-dij[i,0]*z[i-1]+self.Q*(1-z[i-1])>=0
                            ,name="R10_"+str(i-1))
            
        #(11)
        
        for i in range(len(Vset)):
            for j in range(len(self.Gset)):
                if (i!=1+j+len(self.Cset)):
                    model.addConstr(p[i]-dij[i,1+j+len(self.Cset)]*
                                    x[i,1+j+len(self.Cset)]+self.Q*
                                    (1-x[i,1+j+len(self.Cset)])>=0,
                                    name="R11_("+str(i)+","+str(1+j+len(self.Cset))+")")
        

         
           

                    
                   

        #(12)
        
        model.addConstr(t[0]==len(Vset),name="R12_("+str(0)+")" )
        for j in range(1,len(Vset)):
            for i in range(len(Vset)):
                if (i!=j):
                    model.addConstr(t[j] <= t[i] - x[i,j] +
                                  (1-x[i,j])*len(Vset),
                                   name="R12_("+str(i)+","+str(j)+")")   
                    
        #(13)
        for j in range(len(self.Gset)):
            model.addConstr(w[j]>=0,name="R13_"+str(j))

        #(14)
        for j in range(len(self.Gset)):
            model.addConstr(w[j]<=len(Vset),name="R14_"+str(j))               
                    
        
        model.update()    
        """  Save the Lp model"""
        model.write(lpfilename)   

        return model

    def OptimizeVANTProblem(self,model,filesolname):
        
        print('ops')
        model.optimize()
        #print(m.getAttr('x',m.getVars()))
        model.write(filesolname)
        
        if (GRB.OPTIMAL == 2):
            print('Optimal solution found!')
        else:
            print('Optimal solution not found!')

  
        return model     

    def GetNumSolutionValues(self,fileSolname):


        gtam=1+len(self.Cset)+len(self.Gset)
        ytam=len(self.Gset)
        
        tamx=gtam*gtam - gtam - gtam
        x=np.zeros((gtam,gtam))
        y=np.zeros((ytam,1))
        z=np.zeros((gtam-1,1))
        w=np.zeros((ytam,1))
        
        #print('tamx: '+str(tamx))
        
        countx=0;
        with open(fileSolname,'r') as f:
            line = f.readline()
            numbers=re.findall(r"[-+]?\d*\.\d+|\d+", line)
            Fx=numbers[0]
            #print('Fx: '+str(Fx))
            count=0
            #for i in range(tamx):
                #print(re.findall('x', line))    
            for line in f:    
            
                
                if 'x' in line:
                    numbers=re.findall(r"[-+]?\d*\.\d+|\d+", line)
                    g=np.int(numbers[0])
                    h=np.int(numbers[1])
                    x[g,h]=numbers[2] 
                    #print('x['+str(g)+','+str(h)+']='+str(x[g,h]))
                        
                
                if 'y' in line:
                    numbers=re.findall(r"[-+]?\d*\.\d+|\d+", line)
                    g=np.int(numbers[0])
                    y[g]=numbers[1]
                    #print('y['+str(g)+']='+str(y[g]))
                    
                if 'z' in line:
                    numbers=re.findall(r"[-+]?\d*\.\d+|\d+", line)
                    g=np.int(numbers[0])
                    z[g]=numbers[1]
                    #print('z['+str(g)+']='+str(y[g]))  
      
                if 'w' in line:
                    numbers=re.findall(r"[-+]?\d*\.\d+|\d+", line)
                    g=np.int(numbers[0])
                    w[g]=numbers[1]              
                
            """                
                line=f.readline()
                
            for i in range(ytam):
                numbers=re.findall(r"[-+]?\d*\.\d+|\d+", line)
                g=np.int(numbers[0])
                y[g]=numbers[1]           
            """

        return (Fx,x,y,z,w)    
        
    def PrintSolution(self,x,y,z,w):

            lat0=-2.5705308
            latmax=-2.5615587
            long0=-44.3630242
            longmax=-44.3434114
            R=6371
                
            print('')
            print('---------- Solution ------------')
            G=nx.DiGraph()
            G2=nx.Graph()
            N=5
            Instancia=PatiosNorteSul(0)
            (m,redlat,redlon,xline,yline)=Instancia.GetInspectionNodesFromMap(N)
            redx,redy=m(redlon,redlat)
            Aux=ConverterFunctions()
                
            lonbase0=long0 + (self.Onode[0,0]*180)/(R*np.pi*np.cos(lat0*(np.pi/180)))
            latbase0=lat0 + (self.Onode[0,1]*180)/(R*np.pi)
            x0,y0=m(lonbase0,latbase0)
            
            G.add_node(0,pos=(x0,y0))
                
            (latC,lonC)=Aux.CartetesianToGeograph(self.Cset[:,0],self.Cset[:,1],long0,lat0)
            xC,yC=m(lonC,latC)
            for i in range(len(self.Cset)):
                G.add_node(i+1,pos=(xC[i],yC[i]))
            
            (latG,lonG)=Aux.CartetesianToGeograph(self.Gset[:,0],self.Gset[:,1],long0,lat0)
            xG,yG=m(lonG,latG)
            for i in range(len(self.Gset)):      
                    G.add_node(i+1+len(self.Cset),pos=(xG[i],yG[i]))       
        
                
            """ Arestas """
           
            Vset=self.ComputeVset()
            Vlat=np.zeros(len(Vset))
            Vlat[0]=latbase0
            for i in range(1,len(self.Cset)+1):
                Vlat[i]=latC[i-1]
            for i in range(len(self.Gset)):
                Vlat[i+len(self.Cset)+1]=latG[i]
                
            Vlon=np.zeros(len(Vset))
            Vlon[0]=lonbase0
            for i in range(1,len(self.Cset)+1):
                Vlon[i]=lonC[i-1]
            for i in range(len(self.Gset)):
                Vlon[i+len(self.Cset)+1]=lonG[i]    
               
            count=0

            for i in range(len(Vset)):
                for j in range(len(Vset)):
                    if i!=j:
                        if (x[i][j] == 1):
        
                           lona=Vlon[i]
                           lata=Vlat[i]
                           lonb=Vlon[j]
                           latb=Vlat[j] 
                           vetx=np.linspace(lona,lonb,100)
                           vety=np.linspace(lata,latb,100)
                               
                           xEd,yEd=m(vetx,vety)
                           dx=lonb-lona
                           dy=latb-lata
                           #plt.arrow(lona,lata,dx,dy,scale=2**.5)
                           G.add_edges_from([(i,j)])
                           #POS={}
                           #POS['a']=(lona,lata)
                           #POS['b']=(lonb,latb)
                           #nx.draw_networkx(G,POS)
            pos=nx.get_node_attributes(G,'pos')

            EdgeCon=G.edges()
            print(EdgeCon)
            labels = []
            nx.draw_networkx_edges(G,pos,with_labels = True,edgelist=EdgeCon,edge_color='b',arrowsize=5,width=0.7,node_size=100,label='egdeb')


            for i in range(len(self.Cset)):
                if z[i]==1:
                    G2.add_edges_from([(i+1,0)])
                          
            nx.draw(G2,pos,nodelist=[],edgelist=G2.edges(),edge_color='r',style='dashed',arrowsize=5,width=0.8,node_size=100,label='Back edge')
                     
                           
            m.scatter(x0,y0,s=100, marker='H', edgecolor='blue', linewidth='2',facecolor='white',label='Depot')
            m.scatter(xC,yC,s=30, marker='o', edgecolor='blue', linewidth='1',facecolor='red',label='Select critical locations')
            
            
            tamynotsel=len(y)-np.sum(y)
            xGnotsel=np.zeros(int(tamynotsel))
            yGnotsel=np.zeros(int(tamynotsel))
            count=0
            for j in range(len(y)):
                if y[j]==0:
                    xGnotsel[count]=xG[j]
                    yGnotsel[count]=yG[j]
                    count=count+1
            
            
            
            
            m.scatter(xGnotsel,yGnotsel,s=40, marker='^', edgecolor='yellow', linewidth='1',facecolor='yellow',label='Battery Supply Stations')
            
            tamysel=np.sum(y)
            xGsel=np.zeros(int(tamysel))
            yGsel=np.zeros(int(tamysel))
            count=0
            for j in range(len(y)):
                if y[j]==1:
                    xGsel[count]=xG[j]
                    yGsel[count]=yG[j]
                    count=count+1
                    
            m.scatter(xGsel,yGsel,s=40, marker='^', edgecolor='orange', linewidth='1',facecolor='orange',label='Active Battery Supply Stations')    
                    

            image = mpimg.imread("patios2PB.jpg")
            m.imshow(image,origin="upper")
            plt.show()
            plt.legend()    
                
            return m
            #plt.figure(figsize=(8, 8))
            #m.scatter(redx,redy,s=5, marker='o', edgecolor='red', linewidth='1',facecolor='red')
            #m.scatter(xC,yC,s=10, marker='o', edgecolor='blue', linewidth='1',facecolor='yellow')
            #m.scatter(xG,yG,s=20, marker='^', edgecolor='m', linewidth='2',facecolor='m')
            #m.scatter(x0,y0,s=100, marker='H', edgecolor='blue', linewidth='2',facecolor='white')
            #m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2500, verbose= True,alpha= .6)                