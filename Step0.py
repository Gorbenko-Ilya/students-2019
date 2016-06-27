%matplotlib inline 

import numpy as np
import math as math
import matplotlib.pyplot as plt

n=1800 #number of points
tau=n//50 #width of the puls
t0=10.0*tau #delay of the source
tot_time=int(n+t0)
source_point=n//2

def source(t, t0, tau):
    return math.exp(-(t-t0)**2/(2.0 * tau**2))

def drawplot(z, ex, hy, q):
    fig = plt.figure()
    plt.title("After t=%i"%q)
    plt.grid(True)
    plt.xlabel(u'Coordinate z')
    plt.ylabel(u'Function')
    ax = fig.add_subplot(211)
    ax.plot(z, ex, '-', color='blue', linewidth=2, label=u'Ex')
    ax.plot(z, hy, '--', color='red', linewidth=2, label=u'Hy')
    bx = fig.add_subplot(212)
    bx.plot(z, ex, '-', color='blue', linewidth=2, label=u'Ex')
    plt.savefig("step0-at-time-%i.png"%q, fmt='png')
    plt.draw()

ex=np.zeros(n)
hy=np.zeros(n)
z=np.linspace(0,n-1,n)

for q in range(tot_time):
    hy[:-1] += ex[1:] - ex[:-1]
    ex[1:] += hy[1:]-hy[:-1]
    ex[source_point] += source(q,t0,tau)
    if q % int(n/20)==0 or q+5>tot_time:
        drawplot(z, ex, hy, q)
