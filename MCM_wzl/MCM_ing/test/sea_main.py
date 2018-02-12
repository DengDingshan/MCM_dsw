import reflection_parameter as Ocean
import numpy as np
import params as bp
import generate as bg
import smooth_coefficient as sc

# parameters about the ocean reflextion coefficient.
theta = 30./180. * np.pi   # the angle of incidence
f = 13.			# MHz
hrms = 2.4		# waves' RMS heights
a = Ocean.parameter(theta, f, hrms)
reflection = a.reflection()
print (reflection)
import matplotlib.pyplot as plt

for ii in range (11):
	temp = []
	plt.figure()
	for i in range(1000):

		# parameters about the smooth aera rate
		hrms = 2.4		# pay attention to be same
		hurst = 0.1*ii+0.5		# characterization of the smoothness of waves
		surface_params = bp.SelfAffineParameters(hrms, hurst)
		N_power_of_two = 9 						# length of the map is 2^power
		surface_sample = bg.self_affine(surface_params, N_power_of_two)
		smooth = sc.run(surface_sample)
		temp.append(np.log10(smooth * reflection)*10)
		print (i)

	plt.hist(temp, 50, normed=0, facecolor='green', alpha=0.5)
	plt.savefig("hist "+str(hurst)+".png")

# print smooth
# print np.log10(smooth * reflection)*10
