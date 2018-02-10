import numpy as np 

class SWLoss:
	def __init__(self, Lb0, f, R, Phi, Ne, Alpha):
		self._Lb = Lb0
		self._f = f 
		self._R = R
		self._Phi = Phi /180. * np.pi 
		self._Lbf = 0
		self._La = 0
		self._Ne = Ne
		self._Chi = 0
		self._Alpha = Alpha/180.*np.pi
		print Alpha/180., self._Alpha
		self._deff = 0
		self._Chi = -80.8*self._Ne/self._f**2. 
		self._Ij = (1+0.037*self._R)*(np.cos(0.881*self._Chi))
		self._deff = 200. / np.cos(self._Ij)
		self._Lbf = 32.45 + 20.*np.log10(self._f) + 20.*np.log10(self._deff)
		# print "Lbf ",self._Lbf, np.log(self._f*0.001), np.log(self.deff())
		self._fH = 0.012333 * self._Phi + 0.892778
		self._Phij = np.pi / 2. - self._Alpha
		self._La = 677.2 * self._Ij/(((self._f + self._fH)**2 + 10.2)*np.cos(self._Phij))
		self._Lb = self._La + self._Lbf

	def Lb(self):
		return self.Lb
class 
SWL = SWLoss(0, 13., 0., 30., 1., 60.)
print "Lb", SWL._Lb
print "La", SWL._La
print "Lbf", SWL._Lbf
print "fH", SWL._fH
print "Ij", SWL._Ij
print "deff", SWL._deff
print "Phij", SWL._Phij / np.pi * 180.
print "chi", SWL._Chi



