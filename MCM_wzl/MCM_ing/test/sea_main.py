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

mean_figure = []
Process = []
for ii in range (11):
	temp = []
	plt.figure()
<<<<<<< HEAD
	for i in range(1000):

=======
	for i in range(20):
		
>>>>>>> 3236acaed277ec916104cefaad81916cf77afe92
		# parameters about the smooth aera rate
		hrms = 2.4		# pay attention to be same
		hurst = 0.1*ii+0.5		# characterization of the smoothness of waves
		surface_params = bp.SelfAffineParameters(hrms, hurst)
		N_power_of_two = 9 						# length of the map is 2^power
		surface_sample = bg.self_affine(surface_params, N_power_of_two)

		smooth = sc.run(surface_sample)
		temp.append(np.log10(smooth * reflection)*10)
		print (i)

<<<<<<< HEAD
	plt.hist(temp, 50, normed=0, facecolor='green', alpha=0.5)
	plt.savefig("hist "+str(hurst)+".png")

# print smooth
# print np.log10(smooth * reflection)*10
=======
	mean_figure.append(np.mean(np.array(temp)))
	Process.append(i)
	plt.hist(temp, 20, normed=0, facecolor='green', alpha=0.5) 
	plt.savefig("hist "+str(hurst)+".png")
	
# plt.figure()
# plt.plot(Process,mean_figure)
# plt.savefig('plottt.png')



>>>>>>> 3236acaed277ec916104cefaad81916cf77afe92
