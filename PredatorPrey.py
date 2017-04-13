#Numerical solutions to a simple predator- prey model, including demonstrations 
# of convergence criteria.

## dx
## -- = ax -bxy
## dt
##
## dy
## -- = -cy -dxy
## dt
##
#Where a, b, c, d are 
#Species X is prey, Y is predator
import numpy as np
import matplotlib.pyplot as plt


dt= .001 #timestep
Xinit = .1 #initial condition
Yinit = .1 #initial condition
#equation parameters
a= 1
b=1
c= 1
d= 1
timesteps = 10000
T= np.arange(timesteps+1)
X= np.empty(timesteps+1)
Y= np.empty(timesteps+1)

#apply initial conditions
X[0]=Xinit
Y[0]=Yinit

for i in range(0,timesteps):
    X[i+1]= dt*(a* X[i] - b*X[i]*Y[i]) +X[i]
    Y[i+1]= dt*(-c* Y[i] + d*Y[i]*X[i]) +Y[i]



fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(T,X)
ax1.plot(T,Y)
plt.show()

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(Y,X)