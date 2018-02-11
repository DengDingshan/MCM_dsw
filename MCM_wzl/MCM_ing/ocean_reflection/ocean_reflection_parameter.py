import numpy as np

class parameter:
	def __init__(self, seta, f, hrms):
		self._jdconst = 80
		self._seta, self._f, self._hrms = seta, f, hrms
		# print self._seta, self._f, self._hrms
		self._c=3*(10**8)

		return

	def reflection(self):
		self._fresnel_V = (self._jdconst*np.sin(self._seta)-(self._jdconst-np.cos(self._seta)**2)**(0.5))/\
							(self._jdconst*np.sin(self._seta)+(self._jdconst-np.cos(self._seta)**2)**(0.5))
		# print self._fresnel_V
		
		self._ps=2*((2*np.pi*self._hrms*np.sin(self._seta)*self._f*1e6)/self._c)**2
		if self._ps <= 34:
			self._rou = np.exp(-self._ps)*np.i0(self._ps)
		else:
			return 0

		# print self._ps, self._rou

		self._mirreflect=self._fresnel_V*self._rou

		return self._mirreflect