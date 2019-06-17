# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:31:40 2018

@author: Roberto G. Ribeiro
"""
import numpy as np
import math

class ConverterFunctions(object):
    

    def GeographToCartesian(self,latmin,lonmin,latobs,lonobs):
        
        R=6371
        
        
        x =(lonobs-lonmin)*((np.pi/180)*R*np.cos(latobs*(np.pi/180)))
        y =(latobs-latmin)*((np.pi/180)*R)
        
       # x = R * np.cos(lat*(np.pi/180)) * np.cos(lon*(np.pi/180))
       # y = R * np.cos(lat*(np.pi/180)) * np.sin(lon*(np.pi/180))
        return x,y
    
    def CartetesianToGeograph(self,vetx,vety,lonmin,latmin):
        
        R=6371
        
        tam=len(vetx)
        lat=np.zeros(tam)
        lon=np.zeros(tam)      
        for i in range(tam):
            x=vetx[i]
            y=vety[i]
            lon[i]=lonmin + (x*180)/(R*np.pi*np.cos(latmin*(np.pi/180)))
            lat[i]=latmin + (y*180)/(R*np.pi)
            
        
        return lat,lon
        
        
        
       #  a2 = a1 + (x*180)/(R*pi*cos(b1))
# b2 = b1 + (y*180)/(R*pi)



