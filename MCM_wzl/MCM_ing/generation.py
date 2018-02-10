import brown.params as bp
import brown.generate as bg

surface_params = bp.self_affine_default_parameters()
N_power_of_two = 9
surface = bg.self_affine(surface_params, N_power_of_two)
print surface