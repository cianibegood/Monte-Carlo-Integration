"""
The code computes the integral of a function via a Monte Carlo method
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
import time
#%% function to be integrated
def funzione(x):
    y=3*x**2+6
    return y
#%%
#Parameters
a=-1
b=1
N=10000
xlist=np.linspace(a,b,10000)
ylist=funzione(xlist)
ymax=np.max(ylist)
ymin=np.min(ylist)
#%%
fig1=plt.figure(figsize=(8,6))
plt.plot(xlist, ylist, color='blue', linewidth=2.0)
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$y$', fontsize=16)
plt.show()
#%%
def MCintegrate(x1,x2,Nsamp, y1, y2):
    xrand=np.random.uniform(size=Nsamp)*(b-a)+a
    yrand=np.random.uniform(size=Nsamp)*(y2-y1)+y1
    z=0
    for k in range (0, Nsamp):
        if yrand[k]<=funzione(xrand[k]) and yrand[k]>=0:
            z+=1
        elif yrand[k]>funzione(xrand[k]) and yrand[k]<0:
            z-=1
    if ymin>=0:
        z=z/Nsamp*(y2-y1)*(x2-x1) + ymin*(x2-x1)
    elif ymax<0:
        z=z/Nsamp*(y2-y1)*(x2-x1) + ymax*(x2-x1)
    else:
        z=z/Nsamp*(y2-y1)*(x2-x1) 
    return z
#%%
print(MCintegrate(a,b,N, ymin, ymax))
