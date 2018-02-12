import ocean_reflection_parameter as Ocean 
import numpy as np
a = Ocean.parameter(30./180.* np.pi, 13., 2.4)
print a.reflection()
