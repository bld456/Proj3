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
#Where a, b, c, d are species dependent constants 
#Species X is  prey population and  Y is predator population
import numpy as np
import matplotlib.pyplot as plt


dt= .001 #timestep
timesteps = 60000 #number of timesteps

Xinit = 2 #initial condition
Yinit = 13#initial condition

#equation parameters
a= 1
b=1
c= 1
d= 1



T= np.arange(timesteps+1)
X= np.empty(timesteps+1)
Y= np.empty(timesteps+1)

#apply initial conditions
X[0]=Xinit
Y[0]=Yinit


# solution using for loop, forwards differences
for i in range(0,timesteps):
    X[i+1]= dt*(a* X[i] - b*X[i]*Y[i]) +X[i]
    Y[i+1]= dt*(-c* Y[i] + d*Y[i]*X[i]) +Y[i]






fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(T,X)
ax1.plot(T,Y)
plt.xlabel('Time')
plt.ylabel('Population size')
plt.title('Predator - prey model, forwards differences')
plt.show()


