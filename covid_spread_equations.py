#Script to plot an example of Covid spread in a population using the SEIR infectious disease model.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns basic differential equations of Covid SEIR spread model.
def model(z,t):
    beta = 0.5   #Infection rate
    alpha = 0.5  #Incubation rate
    gamma = 0.07 #Removal rate 
    roe = 0.7    #Reduced spread factor
    
    s = z[0]    #Susceptible population fraction
    e = z[1]    #Exposed population fraction
    i = z[2]    #Infected population fraction
    r = z[3]    #Removed population fraction

    #Differential equations of SEIR model
    dsdt = -roe*beta*s*i
    dedt = roe*beta*s*i - alpha*e
    didt = alpha*e - gamma*i
    drdt = gamma*i
    dzdt = [dsdt,dedt,didt,drdt]
    return dzdt

r0 = 0.15  #Initial natural immunity
i0 = 1/1000 # Initial infected fraction
s0 = 0.2 #Percent of suspectible indiviuals
e0  = 1 - r0 -i0 - s0 #Initial exposed individuals fraction

# initial conditions
z0 = [s0,e0,i0,r0]

# time points (span of days)
t = np.linspace(0,200)

# solve ODEs
z = odeint(model,z0,t)

#Initial population size
N = 10000

# plot results
plt.plot(t,N*z[:,0],'b-',label='Suspectible People')
plt.plot(t,N*z[:,1],'r--',label=r'Exposed People')
plt.plot(t,N*z[:,2],'g--',label=r'Infected People')
plt.plot(t,N*z[:,3],'p--',label=r'Removed People')
plt.ylabel('Number of People')
plt.xlabel('Time (days)')
plt.legend(loc='best')
plt.show()


