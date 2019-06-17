# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:50:12 2018

@author: Roberto G Ribeiro
"""

# Nessecary Imports
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.lines as mlines
from ConverterFunctions import ConverterFunctions


import numpy as np
import math

class PatioNorte(object):
    
    def __init__(self,Nnodes):
        self.Nnodes=Nnodes
        
    def GetInspectionNodesFromMap(self,N):
        
        m = Basemap(llcrnrlat = -2.5705308,
            llcrnrlon = -44.3630242,
            urcrnrlat = -2.560502,
            urcrnrlon = -44.3434114,
           resolution='h')

        lat0=-2.5705308
        latmax=-2.5615587
        long0=-44.3630242
        longmax=-44.3434114

        Aux=ConverterFunctions()
        (xmax,ymax)=Aux.GeographToCartesian(lat0,long0,latmax,longmax)
        #N=20
        #Npasso=100
        #passoy=(ymax)/Npasso
        #passox=(xmax)/Npasso


        """ rota 1"""
        #-2,567411	-44,357108 ponto mais a esquerda
        #-2,567197	-44,346508 ponto mais a direita

        lata=-2.567311
        latb=-2.567272
        longa=-44.357108
        longb=-44.346508

        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
    
    
        yline1 = np.linspace(ya,yb,N)
        xline1 = np.linspace(xa,xb,N)
    
    
    
        """ rota 2"""
        
        lata=-2.567092
        latb=-2.567072
        longa=-44.357108
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline2 = np.linspace(ya,yb,N)
        xline2 = np.linspace(xa,xb,N)
        
        yline=np.concatenate((yline1,yline2))
        xline=np.concatenate((xline1,xline2))
        
        """ rota 3"""
        
        lata=-2.566570
        latb=-2.566590
        longa=-44.357808
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline3 = np.linspace(ya,yb,N)
        xline3 = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline3))
        xline=np.concatenate((xline,xline3))
        
        """ rota 4"""
        
        lata=-2.566370
        latb=-2.566390
        longa=-44.357808
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline4 = np.linspace(ya,yb,N)
        xline4 = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline4))
        xline=np.concatenate((xline,xline4))
        
        """ rota 5"""
        
        lata=-2.565906
        latb=-2.565906
        longa=-44.358686
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline5 = np.linspace(ya,yb,N)
        xline5 = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline5))
        xline=np.concatenate((xline,xline5))
        
        """ rota 6"""
        
        lata=-2.565706
        latb=-2.565706
        longa=-44.358686
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline6 = np.linspace(ya,yb,N)
        xline6 = np.linspace(xa,xb,N)
        
        yline=np.concatenate((yline,yline6))
        xline=np.concatenate((xline,xline6))
        
        """ rota 7"""
        
        lata=-2.565188
        latb=-2.565188
        longa=-44.359352
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline7 = np.linspace(ya,yb,N)
        xline7 = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline7))
        xline=np.concatenate((xline,xline7))
        
        """ rota 8"""
        
        lata=-2.564988
        latb=-2.564988
        longa=-44.359352
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline8 = np.linspace(ya,yb,N)
        xline8 = np.linspace(xa,xb,N)
        
        yline=np.concatenate((yline,yline8))
        xline=np.concatenate((xline,xline8))
        
        """ rota 9"""
        
        lata=-2.564492
        latb=-2.564492
        longa=-44.360241
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline9 = np.linspace(ya,yb,N)
        xline9 = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline9))
        xline=np.concatenate((xline,xline9))
        
        """ rota 10"""
        
        lata=-2.564292
        latb=-2.564292
        longa=-44.360241
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline10 = np.linspace(ya,yb,N)
        xline10 = np.linspace(xa,xb,N)
        
        yline=np.concatenate((yline,yline10))
        xline=np.concatenate((xline,xline10))
        
        """ rota 11"""
        
        lata=-2.563723
        latb=-2.563723
        longa=-44.355862
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline11 = np.linspace(ya,yb,N)
        xline11 = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline11))
        xline=np.concatenate((xline,xline11))
        
        """ rota 12"""
        
        lata=-2.563523
        latb=-2.563523
        longa=-44.355862
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline12 = np.linspace(ya,yb,N)
        xline12 = np.linspace(xa,xb,N)
        
        yline=np.concatenate((yline,yline12))
        xline=np.concatenate((xline,xline12))
        
        """ rota 13"""
        
        lata=-2.563077
        latb=-2.563077
        longa=-44.360073
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline13 = np.linspace(ya,yb,N)
        xline13 = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline13))
        xline=np.concatenate((xline,xline13))
        
        """ rota 14"""
        
        lata=-2.562877
        latb=-2.562877
        longa=-44.360073
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline14 = np.linspace(ya,yb,N)
        xline14 = np.linspace(xa,xb,N)
        yline=np.concatenate((yline,yline14))
        xline=np.concatenate((xline,xline14))
        
        """ rota 15"""
        
        lata=-2.562383
        latb=-2.562383
        longa=-44.358563
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline15 = np.linspace(ya,yb,N)
        xline15 = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline15))
        xline=np.concatenate((xline,xline15))
        
        """ rota 16"""
        
        lata=-2.562183
        latb=-2.562183
        longa=-44.358563
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline16 = np.linspace(ya,yb,N)
        xline16 = np.linspace(xa,xb,N)
        yline=np.concatenate((yline,yline16))
        xline=np.concatenate((xline,xline16))
        
        """ rota 17"""
        
        lata=-2.561634
        latb=-2.561634
        longa=-44.358885
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline17 = np.linspace(ya,yb,N)
        xline17 = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline17))
        xline=np.concatenate((xline,xline17))
        
        """ rota 18"""
        
        lata=-2.561434
        latb=-2.561434
        longa=-44.358885
        longb=-44.346508
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline18 = np.linspace(ya,yb,N)
        xline18 = np.linspace(xa,xb,N)
        yline=np.concatenate((yline,yline18))
        xline=np.concatenate((xline,xline18))
        
        (lat,lon)=Aux.CartetesianToGeograph(xline,yline,long0,lat0)
        
        return m,lat,lon,xline,yline