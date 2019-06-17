# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:58:03 2018

@author: Roberto G. Ribeiro
"""

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.lines as mlines
from ConverterFunctions import ConverterFunctions
from PatioNorte import PatioNorte 
from PatiosNorteSul import PatiosNorteSul 
from GaragemEAbs import GaragemEAbs
from ProblemVANT_Aplicable_05_12 import VANTProblem

import numpy as np
import math
import pickle

N=5
Npasso=100




#Instancia2=PatioNorte(0)

Instancia2=PatiosNorteSul(0)
(m,lat,lon,xline,yline)=Instancia2.GetInspectionNodesFromMap(N)
x,y=m(lon,lat)

# garagem

gar=GaragemEAbs()
(lat0,lon0,xnode0,ynode0)=gar.GetO()
(latG,lonG,xGnodes,yGnodes)=gar.GetBatterySupplyNodes(12,lat,lon)
(latC,lonC,xCnodes,yCnodes)=gar.GetInspectionsNodes(20,lat,lon)

x0,y0=m(lon0,lat0)
xG,yG=m(lonG,latG)
xC,yC=m(lonC,latC)

m.scatter(x0,y0,s=100, marker='H', edgecolor='blue', linewidth='2',facecolor='white')
m.scatter(x,y,s=5, marker='o', edgecolor='red', linewidth='1',facecolor='red')
m.scatter(xC,yC,s=10, marker='o', edgecolor='blue', linewidth='1',facecolor='red')

m.scatter(xG,yG,s=20, marker='^', edgecolor='m', linewidth='2',facecolor='m')

#m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2500, verbose= True,alpha= .6)


Cset=np.column_stack((xCnodes,yCnodes))
Gset=np.column_stack((xGnodes,yGnodes))
Onode=np.column_stack((xnode0,ynode0))

nG=len(xGnodes)
f1=[1000]*nG
f2=[1000]*nG

W1=1200 # Drone -cost
W2=2000 # Drone -cost
Q1=17664 #Battery autonomy
Q2=19008 #Battery autonomy
Q3=20000 #Battery autonomy

beta1=960*2; # 60 segundos x 3
beta2=770*2; # 35 segundos x 3


Ins1=VANTProblem(Cset,Gset,Onode,W1,Q1,f1,beta1)
Ins2=VANTProblem(Cset,Gset,Onode,W2,Q2,f2,beta2)

#with open('Ins20PerEPhantom.pk1','wb') as output:
 #   pickle.dump(Ins1,output,pickle.HIGHEST_PROTOCOL)
    
#with open('Ins20PerEInspire.pk1','wb') as output:
 #   pickle.dump(Ins2,output,pickle.HIGHEST_PROTOCOL)    