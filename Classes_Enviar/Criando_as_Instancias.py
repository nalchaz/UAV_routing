# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:56:29 2018

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
from gurobipy import *

import numpy as np
import math
import pickle



filename='----NONE---'

objects=[]
with (open(filename+'.pk1','rb')) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
            
Dados=objects[0]
print(Dados.W)

P1=VANTProblem(Dados.Cset,Dados.Gset,Dados.Onode,Dados.W,Dados.Q,Dados.f,Dados.beta)

model=P1.BuildModel(filename+'.lp')

print('----------')
print(filename)