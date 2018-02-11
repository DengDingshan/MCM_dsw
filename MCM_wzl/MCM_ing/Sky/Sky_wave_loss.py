import numpy as np 
class SWLoss:
	def __init__(self, N, f, R, Phi, Ne, Alpha, h):
		self._Lb = 0
		self._f = f 
		self._R = R
		self._Phi = Phi /180. * np.pi 
		self._Lbf = 0
		self._La = 0
		self._Ne = Ne
		self._Chi = 0
		self._Alpha = Alpha/180.*np.pi
		self._deff = 0
		self._N = N
		self._h = 300.
		self._Phij = np.arcsin(np.sin(self._Alpha + 0.5*np.pi)*6371./(6371.+self._h))
		self._Chi = -80.8*self._Ne/self._f**2. 
		self._Ij = (1+0.037*self._R)*(np.cos(0.881*self._Chi))
		self._deff = 200. / np.cos(self._Phij)
		self._Lbf = 32.45 + 20.*np.log10(self._f) + 20.*np.log10(self._deff)
		# print "Lbf ",self._Lbf, np.log(self._f*0.001), np.log(self.deff())
		self._fH = 0.012333 * self._Phi + 0.892778
		self._Phij = np.pi / 2. - self._Alpha
		self._La = 677.2 * self._Ij/(((self._f + self._fH)**1.98 + 10.2)*np.cos(self._Phij))
		self._Lb = self._La + self._Lbf

	def Lb(self):
		for i in range(self._N-1):
			self._Lbf -= 20.*np.log10(self._deff)
			self._Lbf += 20.*np.log10(self._deff*(i+2))
			self._La = self._La / float(i+1) * float(i+2)
			self._Lb = self._La + self._Lbf 
		return self._Lb

fileread = open("information.txt","r").read().split(" ")
N = int(fileread[0])
f = float(fileread[1]) 
R = float(fileread[2]) 
Phi = float(fileread[3]) 
Ne = float(fileread[4])
Alpha = float(fileread[5])
h = float(fileread[6])
SWL = SWLoss(N, f, R, Phi, Ne, Alpha, h)
print "Lb", SWL.Lb()
# print "La", SWL._La
# print "Lbf", SWL._Lbf
# print "fH", SWL._fH
# print "Ij", SWL._Ij
# print "deff", SWL._deff
# print "Phij", SWL._Phij / np.pi * 180.
# print "chi", SWL._Chi




