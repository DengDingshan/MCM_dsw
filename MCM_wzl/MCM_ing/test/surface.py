import numpy as np
import doctest
class Surface(np.ndarray):
    def __new__(cls, input_array, dxy):
        obj = np.asarray(input_array).view(cls)
        obj.dxy = float(dxy)
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            self.dxy = getattr(obj, 'dxy', None)

def rms(surface):
    return np.sqrt(np.mean(surface**2))

def length(surface, axis=0):
    return surface.shape[axis] * surface.dxy

def nominal_area(surface):
    a = 1.0
    for i in range(len(surface.shape)):
        a *= length(surface)
    return a

def shift_to_zero_mean(surface):
    return Surface(surface - np.mean(surface), surface.dxy)

def mean_aperture(surface):
    return np.mean(np.abs(np.subtract(surface, np.max(surface))))

def pore_volume(surface):
    return mean_aperture(surface) * nominal_area(surface)

def scale_to_rms(surface, rms_target):
    rms_current = rms(surface)
    return Surface(surface * (rms_target / rms_current), surface.dxy)

if __name__ == '__main__':
    doctest.testmod()