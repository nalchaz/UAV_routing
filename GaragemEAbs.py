# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:22:45 2018

@author: Roberto G. Ribeiro
"""
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.lines as mlines
from ConverterFunctions import ConverterFunctions
import random

import numpy as np
import math

class GaragemEAbs(object):
    
    def __init__(self):
        self
    
    def GetO(self):
        
        lat0=-2.5705308
        latmax=-2.5615587
        long0=-44.3630242
        longmax=-44.3434114
        
        lata=-2.568579
        longa=-44.352288
        Aux=ConverterFunctions()
        (x0,y0)=Aux.GeographToCartesian(lat0,long0,lata,longa)

        return lata,longa,x0,y0
    
    def GetBatterySupplyNodes(self,Nnodes,lat,lon):
        
        lat0=-2.5705308
        latmax=-2.5615587
        long0=-44.3630242
        longmax=-44.3434114
        Aux=ConverterFunctions()
        tam=len(lat)
       
        latG=np.zeros(Nnodes)
        lonG=np.zeros(Nnodes)
        xG=np.zeros(Nnodes)
        yG=np.zeros(Nnodes)
        
        for i in range(Nnodes):
            pos=random.randint(0,tam-1)
            latG[i]=lat[pos]
            lonG[i]=lon[pos]
            (xG[i],yG[i])=Aux.GeographToCartesian(lat0,long0,latG[i],lonG[i])   
        
        return latG,lonG,xG,yG
    
    
    def GetInspectionsNodes(self,perc,lat,lon):
        
        lat0=-2.5705308
        latmax=-2.5615587
        long0=-44.3630242
        longmax=-44.3434114
        Aux=ConverterFunctions()
        tam=len(lat)
        Nnodes=int(round((perc/100)*tam))
        
        latC=np.zeros(Nnodes)
        lonC=np.zeros(Nnodes)
        xC=np.zeros(Nnodes)
        yC=np.zeros(Nnodes)
        
        for i in range(Nnodes):
            pos=random.randint(-1,tam-1)
            latC[i]=lat[pos]
            lonC[i]=lon[pos]
            (xC[i],yC[i])=Aux.GeographToCartesian(lat0,long0,latC[i],lonC[i]) 
       
        
        return latC,lonC,xC,yC
        
        
        
        