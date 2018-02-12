import numpy as np
import scipy.stats as ss
import matplotlib as mlt

def Gaussian_Vissible(hm,sigma,h0,theta):

    import numpy as np
    import scipy.stats as ss
    def line(h0,theta,x):
        y = h0 + x*np.tan(np.pi/2-theta)
        return y

    h_max = hm + 3*sigma
    delta_x = 0.5
    x = 0;

    output = 1
    if h0 > h_max:
        key = 0
    else:
        key = 1
    while key:
        h_ew = line(h0,theta,x)
        output *= ss.norm(hm,sigma).cdf(h_ew)
        if h_ew >= h_max:
            key = 0
        x += delta_x
        print(x,h_ew)

    return output



visible = np.zeros([12,512**2])
for i in range(12):
    st = str(i+1);
    hm = 0.1+0.2*i
    data = np.load("surface"+ st +".npy")
    for k in range(512):
        for g in range(512):
            output = Gaussian_Vissible(hm,hm,data[k,g],np.pi/6)
            j = k*512+g
            visible[i,j] = output
    figure(1)
    mlt.hist(visible,bin=100)
#print(visible)
