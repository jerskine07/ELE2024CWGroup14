#########################################################
# Problem B
#########################################################
# Variables
import numpy as np
import sympy as sm
import matplotlib.pyplot as plt
import math

m = 0.425
g = 9.81
d = 0.42
delta = 0.65
r = 0.125
R = 53
L0 = 0.120
L1 = 0.25
alpha = 1.2
c=6815
c=1
k = 1880
b = 10.4
theta = np.deg2rad(42)

#########################################################
# B1
num_points=500
xmin = d + (m * g * np.sin(theta) / (k))
xmax = delta
print(xmin)
print(xmax)
xe = np.array((range(100)))
# At equilibrium no acceleration or velocity: x_2=0 x_3=0
x2=0
y=alpha-xe
L=L0+L1*np.exp(-alpha*y)
Ve = np.array
Ve =np.array(np.sqrt((7*m*(R*y+L)^2)*((5*k(xe-d)/(7*m))-(5*g*np.sin(theta)/7))))

plt.plot(xe,Ve)