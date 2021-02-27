#!/usr/bin/env python3 

import matplotlib.pyplot as plt
from math import e, log
from mpl_toolkits.mplot3d import Axes3D

m = 20

inc = 0.0001
n = int(m/inc)

a = [i*inc for i in range(n)]
b = [m - a[i] for i in range(n)]
r = [a[i]**b[i] - (b[i]**a[i]) for i in range(n)]

def plot_vals(x, y, z, proj=None):
    ax = plt.axes(projection=proj)
    ax.set_xlabel("a")
    ax.set_ylabel("b")
    ax.set_zlabel("a^b - b^a")
    #plt.plot(a, b)

    ax.plot3D(x, y, z)
    plt.show()

def newton_raphson(f, df, x, err):
    px = -1
    while abs(x - px) > err:
        px = x
        print("f(x) = {}\nf'(x) = {}".format(f(x), df(x)))
        x = x - f(x)/df(x)
        print("a = {}\nb = {}".format(x, x - 10))
    print("a^b - b^a = {}".format(x**(10 - x) - ((10 - x)**x)))

#Function info
def f(x):
    return x**(10 - x) - (10 - x)**x

def df(x):
    return (x**(10 - x))*((10 - x)/x - log(e, x)) - ((10 - x)**x)*(log(e, 10 - x) - x/(10 - x))

#plot_vals(a, b, r, "3d")
newton_raphson(f, df, 7, 0.001)
