import ocean_reflection_parameter as Ocean 
import numpy as np
import params as bp
import generate as bg
import smooth_coefficient.py as sc

a = Ocean.parameter(30./180.* np.pi, 13., 2.4)
print a.reflection()

surface_params = bp.SelfAffineParameters()
N_power_of_two = 9
surface_sample = bg.self_affine(surface_params, N_power_of_two)

sc_class = sc.smooth(surface_sample)

print sc_class.run()