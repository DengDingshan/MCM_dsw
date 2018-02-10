import params as bp
import generate as bg

surface_params = bp.SelfAffineParameters()
N_power_of_two = 9
for ii in range(10):
	surface = bg.self_affine(surface_params, N_power_of_two)
	file = open("surface"+str(ii)+".txt","w")
	for i in range(len(surface)):
		for j in range(len(surface)):
			file. write (str(surface[i][j])+" ")
		file. write ("\n")
	print ii