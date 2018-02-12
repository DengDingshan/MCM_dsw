import params as bp
import generate as bg
import numpy as np

surface_params = bp.SelfAffineParameters()
N_power_of_two = 9

surface = bg.self_affine(surface_params, N_power_of_two)
# file = open("surface sample.txt","w")
# for i in range(len(surface)):
# 	for j in range(len(surface)):
# 		file. write (str(surface[i][j])+" ")
# 	file. write ("\n")
np.save("surface12.npy",surface)
