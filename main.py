#########################################################
# Problem B
#########################################################
# Variables
import numpy as np
import sympy as sm
import matplotlib.pyplot as plt

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
# At equilibrium no acceleration or velocity: x_2=0 x_3=0
x2=0
num_points = 500
xe = np.linspace(xmin, xmax, num_points)
y=alpha-xe
L=L0+L1*np.exp(-alpha*y)
V = np.sqrt((7*m*(R*y+L)**2)*((5*k*(xe-d)/(7*m))-(5*g*np.sin(theta)/7)))

plt.plot(xe, V)
plt.xlabel('xe')
plt.ylabel('V')
plt.title('Plot to show V between Xmin and Xmax')
plt.grid()
plt.savefig('figures\\B1.eps', format='eps')
plt.show()

#########################

x=0.75*xmin+0.25*xmax
y=alpha-x
L=L0+L1*np.exp(-alpha*y)
V2 = np.sqrt((7*m*(R*y+L)**2)*((5*k*(x-d)/(7*m))-(5*g*np.sin(theta)/7)))

