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
# c=6815*(g*(m^3))/((A^2)*(s^2))
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
xe = (xmin, xmax)
# At equilibrium no acceleration or velocity: x_2=0 x_3=0
x= 1
x2=0
y=alpha-x
L=L0+L1*np.exp(-alpha*y)
Ve = sm.symbols('Ve',real=True)

def sys(Ve,x):
    return (5*c*(Ve)^2)/(7*m*(R*y*L)^2) + (5*g*np.sin(theta))/(7) - (5*k*(xe-d))/(7*m) - (5*b*x2)/(7*m)

