# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:07:14 2018

@author: Roberto G. Ribeiro
"""

# Nessecary Imports
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.lines as mlines
from ConverterFunctions import ConverterFunctions
from PatioNorte import PatioNorte 
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.figure import Figure

import numpy as np
import math

class PatiosNorteSul(object):
    
    def __init__(self,Nnodes):
        self.Nnodes=Nnodes
        
    def GetInspectionNodesFromMap(self,N):
        
        
        
        m = Basemap(llcrnrlat = -2.577630,
            llcrnrlon = -44.362459,
            urcrnrlat = -2.560250,
            urcrnrlon = -44.334902,
           resolution='h')

        
        lat0=-2.577630
        latmax=-2.560250
        long0=-44.362459
        longmax=-44.334902
        
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
        
        pationorte=PatioNorte(0)
        aux,lat,lon,xline,yline=pationorte.GetInspectionNodesFromMap(N*2)
        
        """
        rotas do patio Sul
        """
        
        """ rota 1s """
        
        lata=-2.575100
        latb=-2.575229
        longa=-44.343904
        longb=-44.337371
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline1s = np.linspace(ya,yb,N)
        xline1s = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline1s))
        xline=np.concatenate((xline,xline1s))
        
        """ rota 2s """
        
        lata=-2.574929
        latb=-2.575029
        longa=-44.343904
        longb=-44.337371
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline2s = np.linspace(ya,yb,N)
        xline2s = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline2s))
        xline=np.concatenate((xline,xline2s))

        """ rota 3s """
        
        lata=-2.574391
        latb=-2.574391
        longa=-44.344362
        longb=-44.337371
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline3s = np.linspace(ya,yb,N)
        xline3s = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline3s))
        xline=np.concatenate((xline,xline3s))
        
        """ rota 4s """
        
        lata=-2.574191
        latb=-2.574191
        longa=-44.344362
        longb=-44.337371
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline4s = np.linspace(ya,yb,N)
        xline4s = np.linspace(xa,xb,N)
        
        yline=np.concatenate((yline,yline4s))
        xline=np.concatenate((xline,xline4s))
        

        """ rota 5s """
        
        lata=-2.573577
        latb=-2.573577
        longa=-44.343745
        longb=-44.337371
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline5s = np.linspace(ya,yb,N)
        xline5s = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline5s))
        xline=np.concatenate((xline,xline5s))
        
        """ rota 6s """
        
        lata=-2.573377
        latb=-2.573377
        longa=-44.343745
        longb=-44.337371
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline6s = np.linspace(ya,yb,N)
        xline6s = np.linspace(xa,xb,N)


        
        yline=np.concatenate((yline,yline6s))
        xline=np.concatenate((xline,xline6s))


        """ rota 7s """
        
        lata=-2.572805
        latb=-2.572805
        longa=-44.343908
        longb=-44.337371
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline7s = np.linspace(ya,yb,N)
        xline7s = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline7s))
        xline=np.concatenate((xline,xline7s))
        
        """ rota 8s """
        
        lata=-2.572605
        latb=-2.572605
        longa=-44.343908
        longb=-44.337371
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline8s = np.linspace(ya,yb,N)
        xline8s = np.linspace(xa,xb,N)
        
        yline=np.concatenate((yline,yline8s))
        xline=np.concatenate((xline,xline8s))
        

        """ rota 9s """
        
        lata=-2.575600
        latb=-2.575629
        #lata=-2.572111
        #latb=-2.572111
        longa=-44.343846
        longb=-44.337371
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline9s = np.linspace(ya,yb,N)
        xline9s = np.linspace(xa,xb,N)
        
        
        yline=np.concatenate((yline,yline9s))
        xline=np.concatenate((xline,xline9s))
        
        """ rota 10s """
        
        lata=-2.575800
        latb=-2.575829
        
        #lata=-2.571911
        #latb=-2.571911
        longa=-44.343846
        longb=-44.337371
        
        (xa,ya)=Aux.GeographToCartesian(lat0,long0,lata,longa)
        (xb,yb)=Aux.GeographToCartesian(lat0,long0,latb,longb)
        
        
        yline10s = np.linspace(ya,yb,N)
        xline10s = np.linspace(xa,xb,N)


        
        yline=np.concatenate((yline,yline10s))
        xline=np.concatenate((xline,xline10s))




        (lat,lon)=Aux.CartetesianToGeograph(xline,yline,long0,lat0) 
        

        
        return m,lat,lon,xline,yline
    
            

