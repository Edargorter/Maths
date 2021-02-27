#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt


inc = 0.001

y_dim = 100
x_dim = 100
m = x_dim/2
n = int(m/inc)

x = [i*inc for i in range(n)]

def get_length(v):
    return 4*(math.sqrt((y_dim/2)**2 + v*v)) + x_dim - 2*v
    
l = [get_length(x[i]) for i in range(n)]

print(l)
print("min length: {}".format(min(l)))

plt.plot(x, l)
plt.xlabel("x")
plt.ylabel("total length")
plt.show()
