import pickle

## Problem
# @attributes : 
#	xini : x position of the initial point
#	yini : y position of the initial point
#	x : list of point's x positions
#	y : list of point's y positions
#	distances : distance matrix
class Problem:

	def __init__(self, filename):
		objects=[]
		with (open(filename+'.pk1','rb')) as openfile:
			while True:
				try:
					objects.append(pickle.load(openfile))
				except EOFError:
					break
		Dados = objects[0]

		self.xini = Dados.Onode[0][0]*1000
		self.yini = Dados.Onode[0][1]*1000

		self.x = []
		self.y = []
		for i in range(len(Dados.Cset)):
			self.x = self.x + [Dados.Cset[i][0]*1000]
			self.y = self.y + [Dados.Cset[i][1]*1000]

		self.distances = [[0 for a in range(len(self.x))] for b in range(len(self.x))]			#Distance matrix for fast calculs
		self.distancesALNS = [[0 for a in range(len(self.x))] for b in range(len(self.x))]
		self.distanceIni = []
		self.distanceIniALNS = []


		for i in range(len(self.x)):
			self.distanceIni += [(((self.xini-self.x[i]))**2 + ((self.yini-self.y[i]))**2)**(1/2)]
			self.distanceIniALNS += [(((self.xini-self.x[i]))**2 + ((self.yini-self.y[i]))**2)]

		for i in range(len(self.x)):
			for j in range(len(self.x)):
				self.distances[i][j] = (((self.x[i]-self.x[j]))**2 + ((self.y[i]-self.y[j]))**2)**(1/2)
				self.distancesALNS[i][j] = (((self.x[i]-self.x[j]))**2 + ((self.y[i]-self.y[j]))**2)
		
