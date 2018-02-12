import reflection_parameter as Ocean 
import numpy as np
import params as bp
import generate as bg
import smooth_coefficient as sc

hrms = 2.4		# pay attention to be same
hurst = 1.2		# characterization of the smoothness of waves
surface_params = bp.SelfAffineParameters(hrms, hurst)
N_power_of_two = 9 						# length of the map is 2^power
surface_sample = bg.self_affine(surface_params, N_power_of_two)

# data = np.array(surface_sample)
data = []
for i in range(len(surface_sample)):
	for j in range(len(surface_sample)):
		data.append(surface_sample[i][j]/hrms)

import matplotlib.pyplot as plt
print data[3]
plt.figure()
plt.hist(data, 50, normed=1, facecolor='green', alpha=0.5) 
plt.show()
plt.savefig("guess_plot hurst "+str(hurst)+" hrms "+str(hrms)+".png")